import discord
from discord.ui import View, Button

class LoveInterestPaginator(View):
    def __init__(self, embeds):
        super().__init__(timeout=120)
        self.embeds = embeds
        self.current = 0

    async def send_initial(self, ctx):
        self.message = await ctx.send(embed=self.embeds[self.current], view=self)

    @discord.ui.button(label="Previous", style=discord.ButtonStyle.secondary)
    async def previous(self, interaction: discord.Interaction, button: Button):
        if self.current > 0:
            self.current -= 1
            await interaction.response.edit_message(embed=self.embeds[self.current], view=self)
        else:
            await interaction.response.defer()

    @discord.ui.button(label="Next", style=discord.ButtonStyle.primary)
    async def next(self, interaction: discord.Interaction, button: Button):
        if self.current < len(self.embeds) - 1:
            self.current += 1
            await interaction.response.edit_message(embed=self.embeds[self.current], view=self)
        else:
            await interaction.response.defer()