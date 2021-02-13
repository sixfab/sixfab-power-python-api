
from power_api import SixfabPower, Definition, Event
import time

pms = SixfabPower()
epoch = time.time()

# Remove all events
print("Result removing all Scheduled Event: " + str(pms.remove_all_scheduled_events(200)))

# create power off event
event = Event()
event.id = 1
event.schedule_type = Definition.EVENT_INTERVAL
event.repeat = Definition.EVENT_ONE_SHOT
event.time_interval = 20
event.interval_type = Definition.INTERVAL_TYPE_SEC
event.action = Definition.SOFT_POWER_OFF

result = pms.create_scheduled_event_with_event(event, 500)

print("Create S. Event Result: " + str(result))
print("IDs of Scheduled Events: " + str(pms.get_scheduled_event_ids()))
