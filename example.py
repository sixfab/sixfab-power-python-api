from pms_api import SixfabPMS, Definition
import time

pms = SixfabPMS()

print("Input Temp: " + str(pms.getInputTemp()))
print("Input Voltage: " + str(pms.getInputVoltage()))
print("Input Current: " + str(pms.getInputCurrent()))
# print("Input Power: " + str(pms.getInputPower()))			#Required delay
print("System Temp: " + str(pms.getSystemTemp()))
print("System Voltage: " + str(pms.getSystemVoltage()))
#print("System Current: " + str(pms.getSystemCurrent()))	#Required delay
#print("System Power: " + str(pms.getSystemPower()))		#Required delay
print("Battery Temp: " + str(pms.getBatteryTemp()))
print("Battery Voltage: " + str(pms.getBatteryVoltage()))
print("Battery Current: " + str(pms.getBatteryCurrent()))
print("Battery Power: " + str(pms.getBatteryPower()))
print("Battery Level: " + str(pms.getBatteryLevel()))
print("Battery Health: " + str(pms.getBatteryHealth()))
print("Watchdog Status: " + str(pms.getWatchdogStatus()))
print("Set Watchdog Status Result: " + str(pms.setWatchdogStatus(1)))
print("RGB Animation Result: " + str(pms.setRgbAnimation(1,1,1)))
print("RGB Animation: " + str(pms.getRgbAnimation()))
print("Fan Health: " + str(pms.getFanHealth()))
print("Fan Automation: " + str(pms.getFanAutomation()))
#
#
#
print("RTC: " + str(pms.getRtcTime(Definition.TIME_FORMAT_DATE_AND_TIME)))
print("Watchdog alarm: " + str(pms.askWatchdogAlarm()))

print("Set Battery Design Capacity Result: " + str(pms.setBatteryDesignCapacity(3400)))
print("Battery Design Capacity: " + str(pms.getBatteryDesignCapacity()))
#
#
#
print("Firmware Ver: " + str(pms.getFirmwareVer()))
