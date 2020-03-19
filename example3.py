from pms_api import SixfabPMS, Definition, DayFactors
import time

pms = SixfabPMS()

print("Result creating Scheduled Event: " + str(pms.createScheduledEvent(0,1,2,120,1,(DayFactors.MONDAY | DayFactors.THURSDAY),0)))
print("Result creating Scheduled Event: " + str(pms.createScheduledEvent(1,1,2,120,1,1,0)))