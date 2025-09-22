import asyncio

from ...embed.embed_factory import EmbedFactory
from helpers.study_timer import StudyTimer
from client.sylus_bot_client import bot
from helpers.components.pomodoro_options import PomodoroOptions

@bot.command()
async def pomodoro_command(ctx):
    view = await get_pomodoro_timers()
    prompt_msg = await ctx.send(
        "You'd like to study now? Sure, I'll set a timer for you, kitten. "
        "\nHow long would you like your study sessions to be?",
        view=view
    )
    selected_time = await view.wait_for_selection()
    await prompt_msg.delete()
    await create_timer(ctx, selected_time)

async def create_timer(ctx, time):
    timer = StudyTimer(time['study_timer'])
    bot.loop.create_task(timer.start_timer())
    timer_info = {
        "title": "Study session",
        "time": timer.amount_of_time,
        "li_study_image": "https://64.media.tumblr.com/a8a1d3b1d02a14bdc8503659de9e6bb5/230b80535a738a55-a3/s540x810/d82ab5b39886c1a3c90c966bcb00d4dcba30e064.gifv"
    }
    message = await show_timer_info(ctx, timer_info)
    await edit_embed_periodically(message, timer.amount_of_time)

async def get_pomodoro_timers():
    buttons = PomodoroOptions()
    return buttons

async def show_timer_info(ctx, timer_info):
    embed, file = EmbedFactory.timer_view(timer_info)
    sent_message = await ctx.send(embed=embed, file=file)
    return sent_message

# Consider moving this to embed factory
async def edit_embed_periodically(message, timer_duration):
    for remaining in range(timer_duration, 0, -1):
        embed, file = EmbedFactory.timer_view({
                "title": "Study session",
                "time": remaining,
                "li_study_image": "https://64.media.tumblr.com/a8a1d3b1d02a14bdc8503659de9e6bb5/230b80535a738a55-a3/s540x810/d82ab5b39886c1a3c90c966bcb00d4dcba30e064.gifv"
            })
        await message.edit(embed=embed, attachments=[file])
        await asyncio.sleep(60)
