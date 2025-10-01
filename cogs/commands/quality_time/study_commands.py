from helpers.components.pomodoro_options import PomodoroOptions
from cogs.events.study_events import StudyEvents
from discord.ext import commands

class StudyCommands(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.selected_time = None

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
            study_events = StudyEvents()
            await study_events.on_command(ctx, selected_time)
            await prompt_msg.delete()
        except Exception as e:
            print(f"Creating timer error: {e}")
            raise e