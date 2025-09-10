from client.sylus_bot_client import client
from . import commands
import json
import random

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    with open('resource/messages/triggers.json', 'r') as file:
        data = json.load(file)

    msg_content = message.content.lower()

    for trigger in data.keys():
        if trigger.lower() in msg_content:
            responses = data[trigger]
            if isinstance(responses[0], list):
                responses = [resp[1] for resp in responses]
            response = random.choice(responses)
            await message.channel.send(response)
            break

    if client.user.mentioned_in(message):
        content_lower = message.content.lower()
        if "love interests" in content_lower:
            await message.channel.send(
                "I see you're ready to pick a love interest. I've got a few in stock, "
                "one really stands out from the rest, if I do say so myself.\n Here are the love interests:"
            )
            ctx = await client.get_context(message)
            await commands.embed_command(ctx)
        else:
            await message.channel.send("You're looking for me, kitten?")

    await client.process_commands(message)
