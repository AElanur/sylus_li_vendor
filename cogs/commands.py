import discord
import json
from .embed_paginator.love_interest_paginator import LoveInterestPaginator


def get_love_interest():
    with open('resource/messages/love_interests.json', 'r') as file:
        data = json.load(file)
    return data["love_interests"]


async def embed_command(ctx):
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
    await paginator.send_initial(ctx)
