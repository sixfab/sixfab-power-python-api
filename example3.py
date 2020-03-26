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
#print("RTC: " + str(pms.setRtcTime(1)))
print("RTC.....DT: " + str(pms.getRtcTime(Definition.TIME_FORMAT_EPOCH)))
print("RTC.....DT: " + str(pms.getRtcTime(Definition.TIME_FORMAT_DATE_AND_TIME)))
"""
# Create Scheduled Events 
#print("Result creating Scheduled Event: " + str(pms.createScheduledEvent(2,1,2,70,0,(Definition.SATURDAY | Definition.THURSDAY),3)))
#print("Result creating Scheduled Event: " + str(pms.createScheduledEvent(3,1,2,90,0,(Definition.FRIDAY | Definition.THURSDAY),2)))

# Remove event by using id
#print("Result removing Scheduled Event: " + str(pms.removeScheduledEvent(2)))

# Remove all evnts
#print("Result removing all Scheduled Event: " + str(pms.removeAllScheduledEvents()))