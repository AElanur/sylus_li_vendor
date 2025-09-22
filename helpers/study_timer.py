import asyncio
import time
from datetime import datetime


class StudyTimer:
    default_minutes = 60
    def __init__(self, amount_of_time):
        self.amount_of_time = amount_of_time
        self.time_started = None
        self.time_pause = None
        self.paused = False


    async def start_timer(self):
        timer_amount = self.amount_of_time * self.default_minutes
        while timer_amount:
            await  asyncio.sleep(1)
            timer_amount -= 1

    async def pause_timer(self):
        if self.time_started is None:
            raise ValueError("Timer not started")
        if self.paused:
            raise ValueError("Timer already paused")
        print('Pausing timer')
        self.time_paused = datetime.now()
        self.paused = True

    async def resume_timer(self):
        if self.time_started is None:
            raise ValueError("Timer not started")
        if self.paused:
            raise ValueError("Timer already paused")
        print('Resuming timer')
        pause_time = datetime.now() - self.time_paused
        self.time_started = self.time_started + pause_time
        self.paused = False