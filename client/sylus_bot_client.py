import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.presences = True

client = commands.Bot(command_prefix="!", intents=intents)
