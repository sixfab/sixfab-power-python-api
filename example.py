from power_api import SixfabPower, Definition
import time

api = SixfabPower()

print("RTC.....DT: " + str(api.getRtcTime(Definition.TIME_FORMAT_DATE_AND_TIME, 100)))

