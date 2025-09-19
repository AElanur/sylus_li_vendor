import os
from dotenv import load_dotenv
from client.sylus_bot_client import bot

load_dotenv()
from cogs import events


if __name__ == "__main__":
    bot.run(os.getenv('DISCORD_KEY'))