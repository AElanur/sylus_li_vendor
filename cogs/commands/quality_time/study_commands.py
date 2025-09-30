import asyncio

from ...embed.embed_factory import EmbedFactory
from helpers.study_timer import StudyTimer
from helpers.components.pomodoro_options import PomodoroOptions
from helpers.components.timer_buttons import TimerButtons
from resource.json_readers.readers import get_love_interest
from discord.ext import commands

class StudyCommands(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def study_timer(self, ctx):
        try:
            await ctx.message.delete()
            view = PomodoroOptions()
            prompt_msg = await ctx.send(
                "You'd like to study now? Sure, I'll set a timer for you, kitten. "
                "\nHow long would you like your study sessions to be?",
                view=view
            )
            selected_time = await view.wait_for_selection()
            await prompt_msg.delete()
            await self.create_timer(ctx, selected_time)
        except Exception as e:
            print(f"Creating timer error: {e}")
            raise e

    async def create_timer(self, ctx, time):
        try:
            timer = StudyTimer(time["study_timer"])
            timer.start_timer()
            # Consider changing this to look better!
            timer_info = {
                "time": timer.get_remaining_minutes(),
                "study_image": get_love_interest()
            }
            await self.show_timer_info(ctx, timer, timer_info)
        except Exception as e:
            print(f"Creating timer error: {e}")
            raise e

    @classmethod
    async def show_timer_info(cls, ctx, timer, timer_info):
        try:
            timer_embed = EmbedFactory()
            buttons = TimerButtons(timer)
            embed, file = timer_embed.timer_view(timer_info)
            sent_message = await ctx.send(embed=embed, file=file, view=buttons)
            await cls.edit_embed_periodically(timer_embed, timer, sent_message, timer_info)
        except Exception as e:
            print(f"Timer view error: {e}")
            raise e

    @classmethod
    async def edit_embed_periodically(cls, embed_view, timer, message, timer_info):
        buttons = TimerButtons(timer)
        while not timer.is_finished():
            if timer.paused:
                await asyncio.sleep(5)
                timer_info["time"] = timer.get_remaining_minutes()
                embed, file = embed_view.timer_view(timer_info)
                await message.edit(embed=embed, attachments=[file], view=buttons)
                continue

            remaining_minutes = timer.get_remaining_minutes()
            timer_info["time"] = remaining_minutes
            embed, file = embed_view.timer_view(timer_info)
            await message.edit(embed=embed, attachments=[file], view=buttons)
            await asyncio.sleep(60)

        timer_info["time"] = 0
        embed, file = embed_view.timer_view(timer_info)
        await message.edit(embed=embed, attachments=[file], view=buttons)
