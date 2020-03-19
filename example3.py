from pms_api import SixfabPMS, Definition, DayFactors
import time

pms = SixfabPMS()

# Create Scheduled Events 
#print("Result creating Scheduled Event: " + str(pms.createScheduledEvent(0,1,2,120,1,(DayFactors.MONDAY | DayFactors.THURSDAY),0)))
#print("Result creating Scheduled Event: " + str(pms.createScheduledEvent(1,1,2,120,1,1,0)))

# Remove event by using id
print("Result removing Scheduled Event: " + str(pms.removeScheduledEvent(1)))

# Remove all evnts
#print("Result removing all Scheduled Event: " + str(pms.removeAllScheduledEvents()))