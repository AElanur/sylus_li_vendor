import asyncio

from ...embed.embed_factory import EmbedFactory
from helpers.study_timer import StudyTimer
from helpers.components.pomodoro_options import PomodoroOptions
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
            print(e)

    async def create_timer(self, ctx, time):
        timer = StudyTimer(time["study_timer"])
        self.bot.loop.create_task(timer.start_timer())
        timer_info = {
            "time": timer.amount_of_time,
            "study_image": get_love_interest()
        }
        message = await self.show_timer_info(ctx, timer_info)
        await self.edit_embed_periodically(message, timer_info)

    @staticmethod
    async def show_timer_info(ctx, timer_info):
        embed, file = EmbedFactory.timer_view(timer_info)
        sent_message = await ctx.send(embed=embed, file=file)
        return sent_message

    @staticmethod
    async def edit_embed_periodically(message, timer_info):
        for remaining in range(timer_info["time"], 0, -1):
            timer_info["time"] = remaining
            embed, file = EmbedFactory.timer_view(timer_info)
            await message.edit(embed=embed, attachments=[file])
            await asyncio.sleep(60)
