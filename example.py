from pms_api import SixfabPMS, Definition
import time

pms = SixfabPMS()

'''
print("Battery Temp: " + str(pms.getBatteryTemp()))
time.sleep(0.1)
print("Battery Voltage: " + str(pms.getBatteryVoltage()))
time.sleep(0.1)
print("Battery Current: " + str(pms.getBatteryCurrent()))
time.sleep(0.1)
print("Battery Power: " + str(pms.getBatteryPower()))
time.sleep(0.1)
print("Battery Health: " + str(pms.getBatteryHealth()))
time.sleep(0.1)
print("Battery Level: " + str(pms.getBatteryLevel()))
time.sleep(0.1)
print("Working Mode: " + str(pms.getWorkingMode()))
time.sleep(0.1)
print("Watchdog Status: " + str(pms.getWatchdogStatus()))
'''

'''
print("Fan Health: " + str(pms.getFanHealth()))
time.sleep(0.1)
print("Watchdog alarm: " + str(pms.askWatchdogAlarm()))
time.sleep(0.1)
print("Watchdog Status: " + str(pms.getWatchdogStatus()))
time.sleep(0.1)
print("Working Mode: " + str(pms.getWorkingMode()))
'''

'''
print("RGB Animation: " + str(pms.getRgbAnimation()))
time.sleep(0.1)
print("Fan Automation: " + str(pms.getFanAutomation()))
time.sleep(0.1)
print("RTC: " + str(pms.getRtcTime()))
time.sleep(0.1)
print("Firmware Ver: " + str(pms.getFirmwareVer()))
'''

'''
print("Set Watchdog Status Result: " + str(pms.setWatchdogStatus(1)))
time.sleep(0.1)
print("Set Fan Automation Result: " + str(pms.setFanAutomation(1, 1)))
'''

print("RTC: " + str(pms.getRtcTime(Definition.TIME_FORMAT_DATE_AND_TIME)))