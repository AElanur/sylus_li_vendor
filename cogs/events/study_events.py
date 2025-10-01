from cogs.embed.study_embed import StudyEmbed
from helpers.study_timer import StudyTimer


class StudyEvents:
    def __init__(self):
        pass

    @staticmethod
    async def on_command(ctx, time):
        print("This is reached")
        timer = StudyTimer(time['study_timer'])
        timer.start_timer()
        study_embed = StudyEmbed(timer, ctx)
        await study_embed.create_timer_embed()
