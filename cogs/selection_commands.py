from discord import Interaction, app_commands

from resource.json_readers.readers import get_sylus_responses, get_love_interest, get_sylus_response_upon_picking
from .embed.embed_factory import EmbedFactory
from discord.ext import commands
import random

class SelectionCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def sylus(self, interaction: Interaction):
        print("Your command works, kitten")
        await interaction.response.send_message("Test, testing kitten")

    # # @bot.command(name="pick", description="Pick a love interest")
    # # async def love_interests(interaction: Interaction):
    # #     await interaction.response.send_message(
    # #         "I see you're ready to pick a love interest. I've got a few in stock, "
    # #         "one really stands out from the rest, if I do say so myself.\nHere are the love interests:"
    #     )
    #     await show_interests_info(interaction)

    # @bot.command()
    # async def pick_love_interest(ctx, message_content):
    #     character = get_love_interest()
    #     for love_interest in character["love_interests"]:
    #         if love_interest['name'].lower() in message_content:
    #             chosen = love_interest['name']
    #             sylus_response = get_sylus_response_upon_picking(chosen)
    #             await ctx.send(
    #                 f"{sylus_response}"
    #                 f"\n**Your chosen love interest is: {chosen}**"
    #             )
    #             await show_interest_info(ctx, chosen)

    # @bot.command()
    # async def chosen_interest(self, ctx):
    #     love_interest = get_sylus_responses()
    #     for interest in love_interest.keys():
    #         if interest.lower() in ctx:
    #             responses = love_interest[interest]
    #             if isinstance(responses[0], list):
    #                 responses = [resp[1] for resp in responses]
    #             response = random.choice(responses)
    #             await ctx.send(response)
    #
    # async def show_interests_info(self, interaction):
    #     embed = EmbedFactory.love_interests_info_embed()
    #     await embed.send_initial(interaction)
    #
    # async def show_interest_info(self, ctx, li):
    #     embed = EmbedFactory.chosen_love_interest_info(li)
    #     await ctx.send(embed=embed)