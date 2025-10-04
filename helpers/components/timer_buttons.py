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
                    await (
                        interaction.
                           response.
                           send_message("I've paused the timer for you, kitten. "
                                        "Let me know if you want me to resume it."))
                    await self.pause_timer()
                if btn['button_function'] == "delete":
                    await self.delete_timer()

            button.callback = timer_button_callback
            self.add_item(button)

    async def pause_timer(self):
        self.timer.pause_timer()

    async def resume_timer(self):
        self.timer.resume_timer()

    async def delete_timer(self):
        self.timer.delete_timer()