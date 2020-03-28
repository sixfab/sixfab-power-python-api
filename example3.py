from pms_api import SixfabPMS, Definition
import time

pms = SixfabPMS()

epoch = time.time()
#print("Epoch Time: " + str(int(epoch)))


# RTC
print("RTC: " + str(pms.setRtcTime(int(epoch), 200)))
print("Actual..DT: "+ str(time.strftime("%Y-%m-%d-%H:%M:%S")))
print("RTC.....DT: " + str(pms.getRtcTime(Definition.TIME_FORMAT_DATE_AND_TIME, 100)))
print("RTC.....DT: " + str(pms.getRtcTime(Definition.TIME_FORMAT_EPOCH, 100)))


# -----------------------------------------------------------
# Function for creating scheduling event
# Parameter : uint8 eventID [id]
# Parameter : uint8 scheduleType [time, interval]
# Parameter : uint8 repeat [once, repeated]
# Parameter : uint16 timeOrInterval [exact time[epoch], interval]
# Parameter : uint8 interval_type [seconds, minutes, hours]
# Parameter : uint8 repeatPeriod [day_factor]  	
# Parameter : uint8 action [start, hard shutdown, soft shutdown, hard reboot, soft reboot]
# Return : result
# -----------------------------------------------------------

"""
print("RTC: " + str(pms.setRtcTime(1)))
print("RTC.....DT: " + str(pms.getRtcTime(Definition.TIME_FORMAT_EPOCH)))
print("RTC.....DT: " + str(pms.getRtcTime(Definition.TIME_FORMAT_DATE_AND_TIME)))
"""

# Remove all evnts
print("Result removing all Scheduled Event: " + str(pms.removeAllScheduledEvents(200)))


# Create Scheduled Events
print("Result creating Scheduled Event: " + str(pms.createScheduledEvent(1,2,1,10,1,Definition.EVERYDAY,2,200)))
print("Result creating Scheduled Event: " + str(pms.createScheduledEvent(2,2,1,20,1,Definition.EVERYDAY,2,200)))
print("Result creating Scheduled Event: " + str(pms.createScheduledEvent(3,2,1,30,1,Definition.EVERYDAY,3,200)))
print("Result creating Scheduled Event: " + str(pms.createScheduledEvent(4,2,1,40,1,Definition.EVERYDAY,4,200)))
print("Result creating Scheduled Event: " + str(pms.createScheduledEvent(5,2,1,50,1,Definition.EVERYDAY,5,200)))
print("Result creating Scheduled Event: " + str(pms.createScheduledEvent(6,2,1,60,1,Definition.EVERYDAY,1,200)))
print("Result creating Scheduled Event: " + str(pms.createScheduledEvent(7,2,1,70,1,Definition.EVERYDAY,2,200)))
print("Result creating Scheduled Event: " + str(pms.createScheduledEvent(8,2,1,80,1,Definition.EVERYDAY,3,200)))
print("Result creating Scheduled Event: " + str(pms.createScheduledEvent(9,2,1,90,1,Definition.EVERYDAY,4,200)))
print("Result creating Scheduled Event: " + str(pms.createScheduledEvent(10,2,1,100,1,Definition.EVERYDAY,5,200)))


# Get Active Scheduled Event IDs
print("IDs of Scheduled Events: " + str(pms.getScheduledEventIds(50)))

# Remove event by using id
#print("Result removing Scheduled Event: " + str(pms.removeScheduledEvent(1)))
#print("Result removing Scheduled Event: " + str(pms.removeScheduledEvent(3)))