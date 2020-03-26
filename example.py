from pms_api import SixfabPMS, Definition
import time

pms = SixfabPMS()


print("System Temp: " + str(pms.getSystemTemp()))
print("Fan Speed: " + str(pms.getFanSpeed()))
print("Set Fan Automation Result: " + str(pms.setFanAutomation(20,60)))
print("Fan Health: " + str(pms.getFanHealth()))
print("RGB Animation Result: " + str(pms.setRgbAnimation(2,2,3))) 

epoch = time.time()
#print("Epoch Time: " + str(int(epoch)))

# RTC
print("RTC: " + str(pms.setRtcTime(int(epoch))))
print("Actual..DT: "+ str(time.strftime("%Y-%m-%d-%H:%M:%S")))
print("RTC.....DT: " + str(pms.getRtcTime(Definition.TIME_FORMAT_DATE_AND_TIME)))