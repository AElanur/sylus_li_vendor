import asyncio

from ...embed.embed_factory import EmbedFactory
from helpers.study_timer import StudyTimer
from client.sylus_bot_client import bot
from helpers.components.pomodoro_options import PomodoroOptions
from resource.json_readers.readers import get_love_interest

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
        "time": timer.amount_of_time,
        "study_image": get_love_interest()
    }

    message = await show_timer_info(ctx, timer_info)
    await edit_embed_periodically(message, timer_info)

async def get_pomodoro_timers():
    buttons = PomodoroOptions()
    return buttons

async def show_timer_info(ctx, timer_info):
    embed, file = EmbedFactory.timer_view(timer_info)
    sent_message = await ctx.send(embed=embed, file=file)
    return sent_message

async def edit_embed_periodically(message, timer_info):
    for remaining in range(timer_info['time'], 0, -1):
        embed, file = EmbedFactory.timer_view(timer_info)
        await message.edit(embed=embed, attachments=[file])
        await asyncio.sleep(60)
