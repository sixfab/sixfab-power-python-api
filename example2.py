from pms_api import SixfabPMS, Definition
import time

pms = SixfabPMS()

print("Setting Watchdog Status: " + str(pms.setWatchdogStatus(0)))
print("Getting Watchdog Status: " + str(pms.getWatchdogStatus()))
print("RGB Animation Result: " + str(pms.setRgbAnimation(2,3,3)))
print("RGB Animation: " + str(pms.getRgbAnimation()))
print("Fan Speed Result: " + str(pms.setFanSpeed(1)))
print("Fan Speed: " + str(pms.getFanSpeed()))
print("Set Fan Automation Result: " + str(pms.setFanAutomation(20,60)))
print("Fan Automation: " + str(pms.getFanAutomation()))
print("Result Safe Shutdown Bat Lev.: " + str(pms.setSafeShutdownBatteryLevel(10)))
print("Safe Shutdown Bat Lev.: " + str(pms.getSafeShutdownBatteryLevel()))
print("Result Safe Shutdown Bat Status.: " + str(pms.setSafeShutdownBatteryStatus(0)))
print("Safe Shutdown Bat Status.: " + str(pms.getSafeShutdownBatteryStatus()))
print("Result Bat. Max Char. Level: " + str(pms.setBatteryMaxChargeLevel(90)))
print("Bat. Max Char. Level: " + str(pms.getBatteryMaxChargeLevel()))