import os
import asyncio
from dotenv import load_dotenv
from client.sylus_bot_client import bot
from cogs.selection_commands import SelectionCommands

load_dotenv()

async def main():
    async with bot:
        await bot.add_cog(SelectionCommands(bot))
        await bot.start(os.getenv('DISCORD_KEY'))

@bot.event
async def on_ready():
    await bot.tree.sync()
    print(f'Logged in as {bot.user} ({bot.user.id})')
    print('Commands synced and bot is ready.')

if __name__ == "__main__":
    asyncio.run(main())
