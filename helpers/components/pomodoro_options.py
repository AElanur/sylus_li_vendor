import asyncio

from discord import ButtonStyle
from discord.ui import View, Button
from resource.json_readers.readers import get_pomodoro_timers

class PomodoroOptions(View):
    def __init__(self):
        super().__init__()
        self.times = get_pomodoro_timers()
        self.selected_time = None
        self.interaction_received = asyncio.Event()

        for i, time_value in enumerate(self.times):
            button = Button(label=f"{time_value['study_timer']} minutes", style=ButtonStyle.green, custom_id=f"pomodoro_{i}")

            async def button_callback(interaction, time=time_value):
                await interaction.response.send_message(
                    f"Noted, I'll set the timer to {time['study_timer']} minutes. "
                    f"After each interval you'll have a {time['pause_timer']} minute, break.")
                self.selected_time = time
                self.interaction_received.set()

            button.callback = button_callback
            self.add_item(button)

    async def wait_for_selection(self):
        await self.interaction_received.wait()
        return self.selected_time