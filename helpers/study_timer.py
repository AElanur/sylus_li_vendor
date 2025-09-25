import asyncio
import time
from datetime import datetime


class StudyTimer:
    default_minutes = 60
    def __init__(self, minutes):
        self.total_seconds = minutes * 60
        self.remaining_seconds = self.total_seconds
        self._task = None
        self._start_time = None
        self.paused = False

    async def _run_timer(selfself, seconds):
        await asyncio.sleep(seconds)

    async def start_timer(self):
        if self._task is None or self._task.done():
            self._start_time = datetime.now()
            elapsed = (datetime.now() - self._start_time).total_seconds()
            self.remaining_seconds -= elapsed
            self.paused = False
        else:
            print("Timer already running")

    async def pause_timer(self):
        if self._task and not self._task.done() and not self.paused:
            self._task.cancel()
            elapsed = (datetime.now() - self._start_time).total_seconds()
            self.remaining_seconds -= elapsed
            self.paused = True
            print(f"Timer paused with {self.remaining_seconds:.2f} seconds remaining")
        else:
            print("Timer is not running or already paused")

    async def resume_timer(self):
        if self.paused:
            self._start_time = datetime.now()
            self._task = asyncio.create_task(self._run_timer(self.remaining_seconds))
            self.paused = False
            print(f"Timer resumed with {self.remaining_seconds:.2f} seconds remaining")
        else:
            print("Timer already running")