
from power_api import SixfabPower, Definition, Event
import time

pms = SixfabPower()
epoch = time.time()

print("RTC Time: " + str(pms.get_rtc_time(Definition.TIME_FORMAT_EPOCH)))
print("RTC Time: " + str(pms.get_rtc_time(Definition.TIME_FORMAT_DATE_AND_TIME)))
print("RTC Time: " + str(pms.get_rtc_time(Definition.TIME_FORMAT_DATE)))
print("RTC Time: " + str(pms.get_rtc_time(Definition.TIME_FORMAT_TIME)))
