from pms_api import SixfabPMS, Definition
import time

pms = SixfabPMS()

print("\r\n")
print("************* Input Sensors **************")
print("Input Temp: " + str(pms.getInputTemp()))
print("Input Voltage: " + str(pms.getInputVoltage()))
print("Input Current: " + str(pms.getInputCurrent()))
print("Input Power: " + str(pms.getInputPower()))			#Required delay
print("\r\n")
print("************* System Sensors **************")
print("System Temp: " + str(pms.getSystemTemp()))
print("System Voltage: " + str(pms.getSystemVoltage()))
print("System Current: " + str(pms.getSystemCurrent()))	#Required delay
print("System Power: " + str(pms.getSystemPower()))		#Required delay
print("\r\n")
print("************* Battery **************")
print("Battery Temp: " + str(pms.getBatteryTemp()))
print("Battery Voltage: " + str(pms.getBatteryVoltage()))
print("Battery Current: " + str(pms.getBatteryCurrent()))
print("Battery Power: " + str(pms.getBatteryPower()))
print("Battery Level: " + str(pms.getBatteryLevel()))
print("Battery Health: " + str(pms.getBatteryHealth()))

print("Fan Health: " + str(pms.getFanHealth()))
print("Fan Speed Result: " + str(pms.setFanSpeed(1)))
print("Fan Speed: " + str(pms.getFanSpeed()))

print("Setting Watchdog Status: " + str(pms.setWatchdogStatus(0)))
print("Getting Watchdog Status: " + str(pms.getWatchdogStatus()))
print("RGB Animation Result: " + str(pms.setRgbAnimation(1,3,3)))
print("RGB Animation: " + str(pms.getRgbAnimation()))
print("Set Fan Automation Result: " + str(pms.setFanAutomation(30,60)))
print("Fan Automation: " + str(pms.getFanAutomation()))
print("Result Bat. Max Char. Level: " + str(pms.setBatteryMaxChargeLevel(90)))
print("Bat. Max Char. Level: " + str(pms.getBatteryMaxChargeLevel()))
print("Result Safe Shutdown Bat Lev.: " + str(pms.setSafeShutdownBatteryLevel(10)))
print("Safe Shutdown Bat Lev.: " + str(pms.getSafeShutdownBatteryLevel()))
print("Result Safe Shutdown Bat Status.: " + str(pms.setSafeShutdownBatteryStatus(0)))
print("Safe Shutdown Bat Status.: " + str(pms.getSafeShutdownBatteryStatus()))
print("Button 1 Status: " + str(pms.getButton1Status()))
print("Button 2 Status: " + str(pms.getButton2Status()))

# RTC
print("RTC: " + str(pms.setRtcTime(1254852)))
print("RTC: " + str(pms.getRtcTime(Definition.TIME_FORMAT_DATE_AND_TIME)))

print("Ask Watchdog Alarm: " + str(pms.askWatchdogAlarm()))

# Battery Design Cap
print("Set Battery Design Capacity Result: " + str(pms.setBatteryDesignCapacity(3400)))
print("Battery Design Capacity: " + str(pms.getBatteryDesignCapacity()))

## Create Scheduled Events 
print("Result creating Scheduled Event: " + str(pms.createScheduledEvent(0,1,2,120,1,(Definition.THURSDAY | Definition.FRIDAY),0)))
print("Result creating Scheduled Event: " + str(pms.createScheduledEvent(1,1,2,120,1,1,0)))

# Remove event by using id
print("Result removing Scheduled Event: " + str(pms.removeScheduledEvent(1)))

# Remove all events
print("Result removing all Scheduled Event: " + str(pms.removeAllScheduledEvents()))

# Firmware Ver.
print("Firmware Ver: " + str(pms.getFirmwareVer()))

# Actions
print("Hard Power Off: " + str(pms.hardPowerOff()))
print("Soft Power Off: " + str(pms.softPowerOff()))
print("Hard Reboot: " + str(pms.hardReboot()))
print("Soft Reboot: " + str(pms.softReboot()))