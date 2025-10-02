import discord
from discord.ext import tasks

from cogs.embed.embed_factory import EmbedFactory
from helpers.components.timer_buttons import TimerButtons
from resource.image.study_image import StudyImage
from resource.json_readers.readers import get_love_interest
from io import BytesIO

class StudyEmbed(EmbedFactory):
    def __init__(self, study_timer, ctx):
        super().__init__()
        self.study_timer = study_timer
        self.message = None
        self.update_task = None
        self.ctx = ctx
        self.file = None

    def get_buttons(self):
        return TimerButtons(self.study_timer)

    async def create_timer_embed(self):
        try:
            time = self.study_timer.get_remaining_minutes()
            image_creator = StudyImage(get_love_interest(), time)
            image = image_creator.create_study_image()
            with BytesIO() as image_binary:
                image.save(image_binary, 'PNG')
                image_binary.seek(0)
                self.file = discord.File(fp=image_binary, filename="timer.png")

                self.embed.title = "Study session"
                self.embed.set_image(url="attachment://timer.png")
                self.message = await self.ctx.send(embed=self.embed, file=self.file, view=self.get_buttons())

                self.update_task = self.update_loop.start()

        except Exception as e:
            print(f"Timer view error: {e}")
            raise e

    @tasks.loop(seconds=60)
    async def update_loop(self):
        if self.study_timer.is_finished():
            self.update_task.cancel()
            return

        try:
            time = self.study_timer.get_remaining_minutes()
            image_creator = StudyImage(get_love_interest(), time)
            image = image_creator.create_study_image()
            with BytesIO() as image_binary:
                image.save(image_binary, 'PNG')
                image_binary.seek(0)
                self.file = discord.File(fp=image_binary, filename="timer.png")

                self.embed.title = "Study session"
                self.embed.set_image(url="attachment://timer.png")

            await self.message.edit(embed=self.embed, attachments=[self.file], view=self.get_buttons())
        except Exception as e:
            print(f"Error updating embed: {e}")


