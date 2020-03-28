
from pms_api import SixfabPMS, Definition, Event
import time

pms = SixfabPMS()

epoch = time.time()

event = Event()
event.id = 1
event.schedule_type = Definition.EVENT_INTERVAL
event.repeat = Definition.EVENT_ONE_SHOT
event.time_interval = 20
event.interval_type = Definition.INTERVAL_TYPE_SEC
event.action = Definition.SOFT_POWER_OFF

result = pms.createScheduledEventWithEvent(event, 500)

print("Create S. Event Result: " + str(result))
print("IDs of Scheduled Events: " + str(pms.getScheduledEventIds()))
