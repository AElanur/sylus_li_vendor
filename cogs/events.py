from client.sylus_bot_client import bot
from . import commands

async def handle_mentions(message):
    content_lower = message.content.lower()
    if "pick" in content_lower:
        ctx = await bot.get_context(message)
        await commands.pick_love_interest(ctx, content_lower)
    elif "timer" in content_lower:
        ctx = await bot.get_context(message)
        await commands.start_timer(ctx, content_lower)
    else:
        await message.channel.send("You're looking for me, kitten?")


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    await handle_mentions(message)

    await bot.process_commands(message)
