from discord import Interaction, app_commands

from resource.json_readers.readers import get_sylus_responses, get_love_interest, get_sylus_response_upon_picking
from ...embed.embed_factory import EmbedFactory
from discord.ext import commands
import random

class SelectionCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def pick_interest(self, interaction: Interaction):
        await interaction.response.send_message(
            "I see you're ready to pick a love interest. I've got a few in stock, "
            "one really stands out from the rest, if I do say so myself.\nHere are the love interests:"
        )
        await self.show_interests_info(interaction)

    # !!! For reference: Edit, and apply a button to the embed to pick from that screen,
    # instead of having to type it out. !!!
    # @commands.command()
    # async def pick_love_interest(self, ctx, message_content):
    #     character = get_love_interest()
    #     for love_interest in character["love_interests"]:
    #         if love_interest['name'].lower() in message_content:
    #             chosen = love_interest['name']
    #             sylus_response = get_sylus_response_upon_picking(chosen)
    #             await ctx.send(
    #                 f"{sylus_response}"
    #                 f"\n**Your chosen love interest is: {chosen}**"
    #             )
    #             await self.show_interest_info(ctx, chosen)

    @staticmethod
    async def show_interests_info(interaction):
        embed = EmbedFactory.love_interests_info_embed(interaction)
        await embed.send_initial(interaction)