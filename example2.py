from pms_api import SixfabPMS, Definition
import time

pms = SixfabPMS()

#print("Battery Health: " + str(pms.getBatteryHealth()))
#print("System Current: " + str(pms.getSystemCurrent()))	#Required delay
#print("System Power: " + str(pms.getSystemPower()))		#Required delay
print("Setting Watchdog Status: " + str(pms.setWatchdogStatus(0)))
print("Getting Watchdog Status: " + str(pms.getWatchdogStatus()))
print("RGB Animation Result: " + str(pms.setRgbAnimation(2,3,3)))
print("RGB Animation: " + str(pms.getRgbAnimation()))
print("Fan Speed Result: " + str(pms.setFanSpeed(1)))
print("Fan Speed: " + str(pms.getFanSpeed()))
print("Set Fan Automation Result: " + str(pms.setFanAutomation(30,60)))
print("Fan Automation: " + str(pms.getFanAutomation()))