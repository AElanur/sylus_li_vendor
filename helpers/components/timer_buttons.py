import asyncio

from discord import ButtonStyle
from discord.ui import View, Button
from resource.json_readers.readers import get_timer_buttons
from helpers.study_timer import StudyTimer

class TimerButtons(View):
    def __init__(self, timer: StudyTimer):
        super().__init__()
        self.selected_button = None
        self.timer = timer
        self.interaction_received = asyncio.Event()

        buttons = get_timer_buttons()
        for button_data in buttons:
            button = Button(
                label=button_data["button_icon"],
                style=ButtonStyle.green,
                custom_id=str(button_data["button_id"])
            )

            async def timer_button_callback(interaction, btn=button_data):
                if btn['button_function'] == "pause":
                    await self.pause_timer()

            button.callback = timer_button_callback
            self.add_item(button)

    async def pause_timer(self):
        print("the timer is paused")
        await self.timer.pause_timer()
        return self.timer.amount_of_time

    async def resume_timer(self):
        await self.timer.resume_timer()
        return self.timer.amount_of_time