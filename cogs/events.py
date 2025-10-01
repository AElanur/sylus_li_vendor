from client.sylus_bot_client import bot
from .commands.quality_time import study_commands

# async def handle_mentions(message):
#     content_lower = message.content.lower()
#     if "timer" in content_lower:
#         ctx = await bot.get_context(message)
#         await study_commands.pomodoro_command(ctx)
#     else:
#         await message.channel.send("You're looking for me, kitten?")

@bot.event
async def on_command(message):
    if message.author == bot.user:
        return

    # await handle_mentions(message)

    await bot.process_commands(message)