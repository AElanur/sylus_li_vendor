from datetime import datetime, timedelta


class StudyTimer:
    def __init__(self, minutes):
        self.total_duration = timedelta(minutes=minutes+1)
        self._start_time = None
        self._paused_time = None
        self._accumulated_pause = timedelta(0)
        self.paused = False

    def start_timer(self):
        self._start_time = datetime.now()
        self._accumulated_pause = timedelta(0)
        self.paused = False

    def pause_timer(self):
        if not self.paused:
            self._paused_time = datetime.now()
            self.paused = True

    def resume_timer(self):
        if self.paused:
            pause_duration = datetime.now() - self._paused_time
            self._accumulated_pause += pause_duration
            self.paused = False

    def delete_timer(self):
        self.total_duration = 0

    def get_remaining_minutes(self):
        if not self._start_time:
            return int(self.total_duration.total_seconds() // 60)
        if self.paused:
            elapsed = self._paused_time - self._start_time - self._accumulated_pause
        else:
            elapsed = datetime.now() - self._start_time - self._accumulated_pause

        remaining = self.total_duration - elapsed

        if remaining.total_seconds() < 0:
            return 0
        return int(remaining.total_seconds() // 60)

    def is_finished(self):
        return self.get_remaining_minutes() == 0
