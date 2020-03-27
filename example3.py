from pms_api import SixfabPMS, Definition
import time

pms = SixfabPMS()

epoch = time.time()
#print("Epoch Time: " + str(int(epoch)))

# RTC
#print("RTC: " + str(pms.setRtcTime(int(epoch))))
print("Actual..DT: "+ str(time.strftime("%Y-%m-%d-%H:%M:%S")))
print("RTC.....DT: " + str(pms.getRtcTime(Definition.TIME_FORMAT_DATE_AND_TIME)))


# -----------------------------------------------------------
# Function for creating scheduling event
# Parameter : uint8 eventID [id]
# Parameter : uint8 scheduleType [time, interval]
# Parameter : uint8 repeat [once, repeated]
# Parameter : uint16 timeOrInterval [exact time[epoch], interval]
# Parameter : uint8 interval_type [seconds, minutes, hours, days]
# Parameter : uint8 repeatPeriod [day_factor]  	
# Parameter : uint8 action [start, hard shutdown, soft shutdown, hard reboot, soft reboot]
# Return : result
# -----------------------------------------------------------

"""
print("RTC: " + str(pms.setRtcTime(1)))
print("RTC.....DT: " + str(pms.getRtcTime(Definition.TIME_FORMAT_EPOCH)))
print("RTC.....DT: " + str(pms.getRtcTime(Definition.TIME_FORMAT_DATE_AND_TIME)))
"""
# Create Scheduled Events

#print("Result creating Scheduled Event: " + str(pms.createScheduledEvent(0,2,1,10,1,Definition.EVERYDAY,1)))
#print("Result creating Scheduled Event: " + str(pms.createScheduledEvent(1,2,2,20,1,Definition.EVERYDAY,2)))
#print("Result creating Scheduled Event: " + str(pms.createScheduledEvent(2,2,1,30,1,Definition.EVERYDAY,3)))
#print("Result creating Scheduled Event: " + str(pms.createScheduledEvent(3,2,1,40,1,Definition.EVERYDAY,4)))

"""
print("Result creating Scheduled Event: " + str(pms.createScheduledEvent(4,1,1,25,1,Definition.EVERYDAY,5)))
print("Result creating Scheduled Event: " + str(pms.createScheduledEvent(5,1,1,10,1,Definition.EVERYDAY,1)))
print("Result creating Scheduled Event: " + str(pms.createScheduledEvent(6,1,1,25,1,Definition.EVERYDAY,2)))
print("Result creating Scheduled Event: " + str(pms.createScheduledEvent(7,1,1,10,1,Definition.EVERYDAY,3)))
print("Result creating Scheduled Event: " + str(pms.createScheduledEvent(8,1,1,25,1,Definition.EVERYDAY,4)))
print("Result creating Scheduled Event: " + str(pms.createScheduledEvent(9,1,1,10,1,Definition.EVERYDAY,5)))
"""
# Remove event by using id
#print("Result removing Scheduled Event: " + str(pms.removeScheduledEvent(1)))
#print("Result removing Scheduled Event: " + str(pms.removeScheduledEvent(3)))

# Remove all evnts
#print("Result removing all Scheduled Event: " + str(pms.removeAllScheduledEvents()))