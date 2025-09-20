from io import BytesIO

import discord
from resource.json_readers.readers import get_love_interest, get_specific_li
from ..embed_paginator.love_interest_paginator import LoveInterestPaginator
from resource.image.study_image import create_study_image


class EmbedFactory:
    @staticmethod
    def love_interests_info_embed():
        love_interests = get_love_interest()
        embeds = []

        for info in love_interests:
            embed = discord.Embed(
                title=info["name"],
                color=int(info["color"], 16)
            )
            embed.add_field(name="Age", value=info["age"], inline=True)
            embed.add_field(name="Height", value=info["height"], inline=True)
            embed.add_field(name="Evol", value=info["evol"], inline=False)
            embed.add_field(name="Birthday", value=info["birthday"], inline=True)
            embed.add_field(name="Sign", value=info["sign"], inline=True)
            embed.set_image(url=info["image"])
            embeds.append(embed)

        paginator = LoveInterestPaginator(embeds)
        return paginator

    @staticmethod
    def chosen_love_interest_info(name):
        love_interest = get_specific_li(name)

        embed = discord.Embed(
            title=love_interest["name"],
            color=int(love_interest["color"], 16)            )
        embed.add_field(name="Age", value=love_interest["age"], inline=True)
        embed.add_field(name="Height", value=love_interest["height"], inline=True)
        embed.add_field(name="Evol", value=love_interest["evol"], inline=False)
        embed.add_field(name="Birthday", value=love_interest["birthday"], inline=True)
        embed.add_field(name="Sign", value=love_interest["sign"], inline=True)
        embed.set_image(url=love_interest["image"])
        return embed

    @staticmethod
    def timer_view(timer_info):
        image = create_study_image(timer_info)
        with BytesIO() as image_binary:
            image.save(image_binary, 'PNG')
            image_binary.seek(0)
            file = discord.File(fp=image_binary, filename="timer.png")

            embed = discord.Embed(title=timer_info["title"])
            embed.set_image(url="attachment://timer.png")

            return embed, file