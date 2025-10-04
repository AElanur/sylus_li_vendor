from cogs.embed.study_embed import StudyEmbed
from helpers.study_timer import StudyTimer
from discord.ext import tasks

class StudyEvents:
    def __init__(self, ctx, timer):
        self.ctx = ctx
        self.timer = timer
        self.study_embed = None

    async def start_study_timer(self):
        self.timer = StudyTimer(self.timer['study_timer'])
        self.timer.start_timer()
        self.study_embed = StudyEmbed(self.timer, self.ctx)
        await self.study_embed.create_timer_embed()
        self.edit_embed.start()

    @tasks.loop(seconds=60)
    async def edit_embed(self):
        if self.timer.is_finished():
            await self.ctx.message.delete()
            self.edit_embed.cancel()
        elif self.timer.paused:
            self.edit_embed.cancel()
        else:
            await self.study_embed.edit_embed()
