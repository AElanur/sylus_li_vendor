from io import BytesIO

import discord
from resource.json_readers.readers import get_love_interest
from .embed_paginator.love_interest_paginator import LoveInterestPaginator
from resource.image.study_image import StudyImage


class EmbedFactory:
    def __init__(self, title=None, color=None):
        self.embed = discord.Embed(
            title = title,
            color = color,
        )

    def love_interests_info_embed(self):
        try:
            love_interests = get_love_interest()
            embeds = []
            self.embed.title = "Love Interests"
            for info in love_interests:
                self.embed.add_field(name="Age", value=info["age"], inline=True)
                self.embed.add_field(name="Height", value=info["height"], inline=True)
                self.embed.add_field(name="Evol", value=info["evol"], inline=False)
                self.embed.add_field(name="Birthday", value=info["birthday"], inline=True)
                self.embed.add_field(name="Sign", value=info["sign"], inline=True)
                self.embed.set_image(url=info["image"])
                embeds.append(self.embed)

            paginator = LoveInterestPaginator(embeds)
            return paginator
        except Exception as e:
            print(f"Paginator error: {e}")
            raise e

    def timer_view(self, timer_info):
        try:
            image_creator = StudyImage(timer_info)
            image = image_creator.create_study_image()
            with BytesIO() as image_binary:
                image.save(image_binary, 'PNG')
                image_binary.seek(0)
                file = discord.File(fp=image_binary, filename="timer.png")

                self.embed.title="Study session"
                self.embed.set_image(url="attachment://timer.png")

                return self.embed, file
        except Exception as e:
            print(f"Timer view error: {e}")
            raise e
