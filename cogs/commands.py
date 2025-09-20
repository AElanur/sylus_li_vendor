from resource.json_readers.readers import get_sylus_responses, get_love_interest, get_sylus_response_upon_picking
from client.sylus_bot_client import bot
from .embed.embed_factory import EmbedFactory
from helpers.study_timer import StudyTimer
import random

@bot.command()
async def love_interests(ctx):
    await ctx.send(
        "I see you're ready to pick a love interest. I've got a few in stock, "
        "one really stands out from the rest, if I do say so myself.\nHere are the love interests:"
    )
    await show_interests_info(ctx)

@bot.command()
async def pick_love_interest(ctx, message_content):
    character = get_love_interest()
    for love_interest in character["love_interests"]:
        if love_interest['name'].lower() in message_content:
            chosen = love_interest['name']
            sylus_response = get_sylus_response_upon_picking(chosen)
            await ctx.send(
                f"{sylus_response}"
                f"\n**Your chosen love interest is: {chosen}**"
            )
            await show_interest_info(ctx, chosen)

@bot.command()
async def chosen_interest(ctx):
    love_interest = get_sylus_responses()
    for interest in love_interest.keys():
        if interest.lower() in ctx:
            responses = love_interest[interest]
            if isinstance(responses[0], list):
                responses = [resp[1] for resp in responses]
            response = random.choice(responses)
            await ctx.send(response)

@bot.command()
async def start_timer(ctx, message_content):
    await ctx.send(
        "You'd like to study now? Sure, I'll set a timer for you, kitten"
    )
    timer = StudyTimer(message_content, 50)
    timer.start_timer()
    timer_info = {
        "title": "Study session",
        "time": timer.amount_of_time,
        "li_study_image": "https://64.media.tumblr.com/a8a1d3b1d02a14bdc8503659de9e6bb5/230b80535a738a55-a3/s540x810/d82ab5b39886c1a3c90c966bcb00d4dcba30e064.gifv"
    }
    print(timer_info)
    await show_timer_info(ctx, timer_info)

async def show_interests_info(ctx):
    embed = EmbedFactory.love_interests_info_embed()
    await embed.send_initial(ctx)

async def show_interest_info(ctx, li):
    embed = EmbedFactory.chosen_love_interest_info(li)
    await ctx.send(embed=embed)

async def show_timer_info(ctx, timer_info):
    embed, file = EmbedFactory.timer_view(timer_info)
    await ctx.send(embed=embed, file=file)