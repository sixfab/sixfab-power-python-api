#!/usr/bin/python3


class Event:
    def __init__(
        self,
        id=0,
        schedule_type=0,
        repeat=0,
        time_interval=0,
        interval_type=0,
        day=0,
        action=0,
    ):
        self.id = id
        self.schedule_type = schedule_type
        self.repeat = repeat
        self.time_interval = time_interval
        self.interval_type = interval_type
        self.day = day
        self.action = action
