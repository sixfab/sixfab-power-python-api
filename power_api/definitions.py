#!/usr/bin/python3


class Definition:
    # Time Format
    TIME_FORMAT_EPOCH = 0
    TIME_FORMAT_DATE_AND_TIME = 1
    TIME_FORMAT_DATE = 2
    TIME_FORMAT_TIME = 3

    # Day factor
    MONDAY = 1 << 0
    TUESDAY = 1 << 1
    WEDNESDAY = 1 << 2
    THURSDAY = 1 << 3
    FRIDAY = 1 << 4
    SATURDAY = 1 << 5
    SUNDAY = 1 << 6
    EVERYDAY = 127

    # Scheduled Event ID Factor
    SE_ID_0 = 1 << 0
    SE_ID_1 = 1 << 1
    SE_ID_2 = 1 << 2
    SE_ID_3 = 1 << 3
    SE_ID_4 = 1 << 4
    SE_ID_5 = 1 << 5
    SE_ID_6 = 1 << 6
    SE_ID_7 = 1 << 7
    SE_ID_8 = 1 << 8
    SE_ID_9 = 1 << 9

    # Set Command Result
    SET_OK = 1
    SET_FAILED = 2

    # Set Command Result
    FAN_HEALTY = 1
    FAN_BROKEN = 2

    # RGB Animation Type
    RGB_DISABLED = 1
    RGB_HEARTBEAT = 2
    RGB_TEMP_MAP = 3

    # RGB Color
    RED = 1
    GREEN = 2
    BLUE = 3
    YELLOW = 4
    CYAN = 5
    MAGENTA = 6
    WHITE = 7
    BLACK = 8

    # RGB Animation Speed
    RGB_SLOW = 1
    RGB_NORMAL = 2
    RGB_FAST = 3

    # Working Mode
    ADAPTER_POWERED_AND_CHARGING = 1
    ADAPTER_POWERED_AND_FULLY_CHARGED = 2
    BATTERY_POWERED = 3

    # Actions
    HARD_POWER_ON =         1
    HARD_POWER_OFF =        2
    SOFT_POWER_OFF =        3
    HARD_REBOOT =           4
    SOFT_REBOOT =           5
    SOFT_POWER_ON =         6

    # Event Schedule Type
    NO_EVENT = 0
    EVENT_TIME = 1
    EVENT_INTERVAL = 2

    # Event Repeat Type
    EVENT_ONE_SHOT = 1
    EVENT_REPEATED = 2

    # IntervalType
    INTERVAL_TYPE_SEC = 1
    INTERVAL_TYPE_MIN = 2
    INTERVAL_TYPE_HOUR = 3

    # Software Action ids
    ACTION_SOFT_SHUTDOWN = 13
    ACTION_SOFT_REBOOT = 14
    NO_SOFT_ACTION = 2

    # Software Action Commands
    C_SOFT_SHUTDOWN = "sleep(5) & sudo shutdown -h now"
    C_SOFT_REBOOT = "sleep(5) & sudo reboot"
