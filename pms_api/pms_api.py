#!/usr/bin/python3

import time
import datetime
from .pms_command import Command
from .definitions import Definition

command = Command()

#############################################################
### Communication Protocol ##################################
#############################################################
bufferSend = list()
bufferRecieve = list()
bufferRecieveIndex = 0

RESPONSE_DELAY = 					100

START_BYTE_RECIEVED = 				0xDC 		# Start Byte Recieved
START_BYTE_SENT = 					0xCD 		# Start Byte Sent
PROTOCOL_HEADER_SIZE =				5
PROTOCOL_FRAME_SIZE =				7
COMMAND_SIZE_FOR_FLOAT = 			11
COMMAND_SIZE_FOR_DOUBLE = 			13
COMMAND_SIZE_FOR_INT16 = 			9
COMMAND_SIZE_FOR_INT32 = 			11
COMMAND_SIZE_FOR_UINT8 = 			8
COMMAND_SIZE_FOR_INT64 = 			15

COMMAND_TYPE_REQUEST = 				0x01
COMMAND_TYPE_RESPONSE = 			0x02

DEVICE_ADDRESS = 0x41      #7 bit address (will be left shifted to add the read write bit)



###########################################
### Private Methods #######################
###########################################

# Function for printing debug message 
def debug_print(message):
	print(message)

# Function for getting time as miliseconds
def millis():
	return int(time.time())

# Function for delay as miliseconds
def delay_ms(ms):
	time.sleep(float(ms/1000.0))

#############################################################
### PMS CLASS ###############################################
#############################################################
class SixfabPMS:
	board = "Sixfab Raspberry Pi UPS HAT"
	
	# Special Characters
	CTRL_Z = '\x1A'
	
	# Initializer function
	def __init__(self):
		debug_print(self.board + " Class initialized!")
 		

	def __del__(self): 
		#GPIO.cleanup()
		print("Class Destructed")
			

	#############################################################
	### API Call Methods ########################################
	#############################################################
	
	# -----------------------------------------------------------
	# Function for getting input temperature
	# Parameter : None
	# Return : float temp [Celcius]
	# -----------------------------------------------------------
	def getInputTemp(self):
		command.createCommand(command.PROTOCOL_COMMAND_GET_INPUT_TEMP)
		command.sendCommand()
		delay_ms(RESPONSE_DELAY)
		raw = command.recieveCommand(COMMAND_SIZE_FOR_INT32)

		temp = int.from_bytes(raw[PROTOCOL_HEADER_SIZE:COMMAND_SIZE_FOR_INT32 - 2], "big")
		return temp / 100


	# -----------------------------------------------------------
	# Function for getting input voltage
	# Parameter : None
	# Return : float voltage [Volt]
	# -----------------------------------------------------------
	def getInputVoltage(self):
		command.createCommand(command.PROTOCOL_COMMAND_GET_INPUT_VOLTAGE)
		command.sendCommand()
		delay_ms(RESPONSE_DELAY)
		raw = command.recieveCommand(COMMAND_SIZE_FOR_INT32)

		voltage = int.from_bytes(raw[PROTOCOL_HEADER_SIZE : COMMAND_SIZE_FOR_INT32 - 2 ], "big")
		return voltage / 100


	# -----------------------------------------------------------
	# Function for getting input current
	# Parameter : None
	# Return : float current [Ampere]
	# -----------------------------------------------------------
	def getInputCurrent(self):
		command.createCommand(command.PROTOCOL_COMMAND_GET_INPUT_CURRENT)
		command.sendCommand()
		delay_ms(RESPONSE_DELAY)
		raw = command.recieveCommand(COMMAND_SIZE_FOR_INT32)

		current = int.from_bytes(raw[PROTOCOL_HEADER_SIZE : COMMAND_SIZE_FOR_INT32 - 2 ], "big")
		return current / 100


	# -----------------------------------------------------------
	# Function for getting input power
	# Parameter : None
	# Return : float power [Watt]
	# -----------------------------------------------------------
	def getInputPower(self):
		command.createCommand(command.PROTOCOL_COMMAND_GET_INPUT_POWER)
		command.sendCommand()
		delay_ms(RESPONSE_DELAY)
		raw = command.recieveCommand(COMMAND_SIZE_FOR_INT32)

		power = int.from_bytes(raw[PROTOCOL_HEADER_SIZE : COMMAND_SIZE_FOR_INT32 - 2 ], "big")
		return power / 100


	# -----------------------------------------------------------
	# Function for getting system temperature
	# Parameter : None
	# Return : float temp [Celcius]
	# -----------------------------------------------------------
	def getSystemTemp(self):
		command.createCommand(command.PROTOCOL_COMMAND_GET_SYSTEM_TEMP)
		command.sendCommand()
		delay_ms(RESPONSE_DELAY)
		raw = command.recieveCommand(COMMAND_SIZE_FOR_INT32)

		temp = int.from_bytes(raw[PROTOCOL_HEADER_SIZE:COMMAND_SIZE_FOR_INT32 - 2], "big")
		return temp / 100


	# -----------------------------------------------------------
	# Function for getting system voltage
	# Parameter : None
	# Return : float voltage [Volt]
	# -----------------------------------------------------------
	def getSystemVoltage(self):
		command.createCommand(command.PROTOCOL_COMMAND_GET_SYSTEM_VOLTAGE)
		command.sendCommand()
		delay_ms(RESPONSE_DELAY)
		raw = command.recieveCommand(COMMAND_SIZE_FOR_INT32)

		voltage = int.from_bytes(raw[PROTOCOL_HEADER_SIZE : COMMAND_SIZE_FOR_INT32 - 2 ], "big")
		return voltage / 1000


	# -----------------------------------------------------------
	# Function for getting system current
	# Parameter : None
	# Return : float current [Ampere]
	# -----------------------------------------------------------
	def getSystemCurrent(self):
		command.createCommand(command.PROTOCOL_COMMAND_GET_SYSTEM_CURRENT)
		command.sendCommand()
		delay_ms(RESPONSE_DELAY)
		raw = command.recieveCommand(COMMAND_SIZE_FOR_INT32)

		current = int.from_bytes(raw[PROTOCOL_HEADER_SIZE : COMMAND_SIZE_FOR_INT32 - 2 ], "big")
		return current / 1000


	# -----------------------------------------------------------
	# Function for getting system power
	# Parameter : None
	# Return : float power [Watt]
	# -----------------------------------------------------------
	def getSystemPower(self):
		command.createCommand(command.PROTOCOL_COMMAND_GET_SYSTEM_POWER)
		command.sendCommand()
		delay_ms(RESPONSE_DELAY)
		raw = command.recieveCommand(COMMAND_SIZE_FOR_INT32)

		power = int.from_bytes(raw[PROTOCOL_HEADER_SIZE : COMMAND_SIZE_FOR_INT32 - 2 ], "big")
		return power / 1000


	# -----------------------------------------------------------
	# Function for getting battery temperature
	# Parameter : None
	# Return : float temp [Celcius]
	# -----------------------------------------------------------
	def getBatteryTemp(self):
		command.createCommand(command.PROTOCOL_COMMAND_GET_BATTERY_TEMP)
		command.sendCommand()
		delay_ms(RESPONSE_DELAY)
		raw = command.recieveCommand(COMMAND_SIZE_FOR_INT32)

		temp = int.from_bytes(raw[PROTOCOL_HEADER_SIZE:COMMAND_SIZE_FOR_INT32 - 2], "big")
		return temp / 100


	# -----------------------------------------------------------
	# Function for getting battery voltage
	# Parameter : None
	# Return : float voltage [Volt]
	# -----------------------------------------------------------
	def getBatteryVoltage(self):
		command.createCommand(command.PROTOCOL_COMMAND_GET_BATTERY_VOLTAGE)
		command.sendCommand()
		delay_ms(RESPONSE_DELAY)
		raw = command.recieveCommand(COMMAND_SIZE_FOR_INT32)

		voltage = int.from_bytes(raw[PROTOCOL_HEADER_SIZE : COMMAND_SIZE_FOR_INT32 - 2 ], "big")
		return voltage / 1000


	# -----------------------------------------------------------
	# Function for getting battery current
	# Parameter : None
	# Return : float current [Ampere]
	# -----------------------------------------------------------
	def getBatteryCurrent(self):
		command.createCommand(command.PROTOCOL_COMMAND_GET_BATTERY_CURRENT)
		command.sendCommand()
		delay_ms(RESPONSE_DELAY)
		raw = command.recieveCommand(COMMAND_SIZE_FOR_INT32)

		current = int.from_bytes(raw[PROTOCOL_HEADER_SIZE : COMMAND_SIZE_FOR_INT32 - 2 ], "big")
		return current / 1000


	# -----------------------------------------------------------
	# Function for getting battery power
	# Parameter : None
	# Return : float power [Watt]
	# -----------------------------------------------------------
	def getBatteryPower(self):
		command.createCommand(command.PROTOCOL_COMMAND_GET_BATTERY_POWER)
		command.sendCommand()
		delay_ms(RESPONSE_DELAY)
		raw = command.recieveCommand(COMMAND_SIZE_FOR_INT32)

		power = int.from_bytes(raw[PROTOCOL_HEADER_SIZE : COMMAND_SIZE_FOR_INT32 - 2 ], "big")
		return power / 1000


	# -----------------------------------------------------------
	# Function for getting battery level
	# Parameter : None
	# Return : int level [%]
	# -----------------------------------------------------------
	def getBatteryLevel(self):
		command.createCommand(command.PROTOCOL_COMMAND_GET_BATTERY_LEVEL)
		command.sendCommand()
		delay_ms(RESPONSE_DELAY)
		raw = command.recieveCommand(COMMAND_SIZE_FOR_INT16)

		level = int.from_bytes(raw[PROTOCOL_HEADER_SIZE : COMMAND_SIZE_FOR_INT16 - 2 ], "big")
		return level

	# -----------------------------------------------------------
	# Function for getting fan health
	# Parameter : None
	# Return : int level [HEALTY, BROKEN]
	# -----------------------------------------------------------
	def getFanHealth(self):
		command.createCommand(command.PROTOCOL_COMMAND_GET_FAN_HEALTH)
		command.sendCommand()
		delay_ms(RESPONSE_DELAY)
		raw = command.recieveCommand(COMMAND_SIZE_FOR_INT16)

		health = int.from_bytes(raw[PROTOCOL_HEADER_SIZE : COMMAND_SIZE_FOR_INT16 - 2 ], "big")
		return health


	# -----------------------------------------------------------
	# Function for getting battery health
	# Parameter : None
	# Return : int health [%]
	# -----------------------------------------------------------
	def getBatteryHealth(self):
		command.createCommand(command.PROTOCOL_COMMAND_GET_BATTERY_HEALTH)
		command.sendCommand()
		delay_ms(RESPONSE_DELAY)
		raw = command.recieveCommand(COMMAND_SIZE_FOR_INT16)

		health = int.from_bytes(raw[PROTOCOL_HEADER_SIZE : COMMAND_SIZE_FOR_INT16 - 2 ], "big")
		return health


	# -----------------------------------------------------------
	# Function for getting fan speed
	# Parameter : None
	# Return : int speed [RPM]
	# -----------------------------------------------------------
	def getFanSpeed(self):
		command.createCommand(command.PROTOCOL_COMMAND_GET_FAN_SPEED)
		command.sendCommand()
		delay_ms(RESPONSE_DELAY)
		raw = command.recieveCommand(COMMAND_SIZE_FOR_INT16)

		rpm = int.from_bytes(raw[PROTOCOL_HEADER_SIZE : COMMAND_SIZE_FOR_INT16 - 2 ], "big")
		return rpm


	# -----------------------------------------------------------
	# Function for setting fan speed
	# Parameter : uint8 status [true, false] 
	# Return : uint8 result [true, false]
	# -----------------------------------------------------------
	def setFanSpeed(self, status):
		command.createSetCommand(command.PROTOCOL_COMMAND_SET_FAN_SPEED, status, 1)
		command.sendCommand()
		delay_ms(RESPONSE_DELAY)
		raw = command.recieveCommand(COMMAND_SIZE_FOR_UINT8)

		result = raw[PROTOCOL_HEADER_SIZE]
		return result


	# -----------------------------------------------------------
	# Function for getting watchdog status
	# Parameter : None
	# Return : int8 status [true, false]
	# -----------------------------------------------------------
	def getWatchdogStatus(self):
		command.createCommand(command.PROTOCOL_COMMAND_GET_WATCHDOG_STATUS)
		command.sendCommand()
		delay_ms(RESPONSE_DELAY)
		raw = command.recieveCommand(COMMAND_SIZE_FOR_UINT8)

		status = raw[PROTOCOL_HEADER_SIZE]
		return status


	# -----------------------------------------------------------
	# Function for setting watchdog status
	# Parameter : uint8 status [true, false] 
	# Return : uint8 result [true, false]
	# -----------------------------------------------------------
	def setWatchdogStatus(self, status):
		command.createSetCommand(command.PROTOCOL_COMMAND_SET_WATCHDOG_STATUS, status, 1)
		command.sendCommand()
		delay_ms(RESPONSE_DELAY)
		raw = command.recieveCommand(COMMAND_SIZE_FOR_UINT8)

		result = raw[PROTOCOL_HEADER_SIZE]
		return result


	# -----------------------------------------------------------
	# Function for setting RGB animation
	# Parameter : uint8 type [DISABLED, HEARTBEAT, TEMP_MAP]
	# Parameter : uint8 color [GREEN, BLUE, RED, YELLOW, CYAN, MAGENTA, WHITE]
	# Parameter : uint8 speed [SLOW, NORMAL, FAST] 
	# Return : uint8 result [true, false]
	# -----------------------------------------------------------
	def setRgbAnimation(self, animType, color, speed):
		
		value = bytearray()
		value.append(int(animType))
		value.append(int(color))
		value.append(int(speed))

		command.createSetCommand(command.PROTOCOL_COMMAND_SET_RGB_ANIMATION, value, 3)
		command.sendCommand()
		delay_ms(RESPONSE_DELAY)
		raw = command.recieveCommand(COMMAND_SIZE_FOR_UINT8)

		result = raw[PROTOCOL_HEADER_SIZE]
		return result



	# -----------------------------------------------------------
	# Function for getting RGB animation
	# Parameter : None
	# Return : byteArray(3) - ledAnimation[animType, color, speed]
	# -----------------------------------------------------------
	def getRgbAnimation(self):
		command.createCommand(command.PROTOCOL_COMMAND_GET_RGB_ANIMATION)
		command.sendCommand()
		delay_ms(RESPONSE_DELAY)
		raw = command.recieveCommand(10)

		animation = bytearray()
		for i in range(3):
			animation.append(raw[PROTOCOL_HEADER_SIZE + i])
		
		return animation


	# -----------------------------------------------------------
	# Function for setting fan automation
	# Parameter : uint8 slow-treshold [celcius]
	# Parameter : uint8 fast-treshold [celcius]
	# Return : result
	# -----------------------------------------------------------
	def setFanAutomation(self, slowTreshold, fastTreshold):

		value = bytearray()
		value.append(int(slowTreshold))
		value.append(int(fastTreshold))

		command.createSetCommand(command.PROTOCOL_COMMAND_SET_FAN_AUTOMATION, value, 2)
		command.sendCommand()
		delay_ms(RESPONSE_DELAY)
		raw = command.recieveCommand(COMMAND_SIZE_FOR_UINT8)

		result = raw[PROTOCOL_HEADER_SIZE]
		return result



	# -----------------------------------------------------------
	# Function for getting fan automation
	# Parameter : None
	# Return : byteArray(2) - fanAutomation[slowTreshold, fastTreshold]
	# -----------------------------------------------------------
	def getFanAutomation(self):
		command.createCommand(command.PROTOCOL_COMMAND_GET_FAN_AUTOMATION)
		command.sendCommand()
		delay_ms(RESPONSE_DELAY)
		raw = command.recieveCommand(9)

		fanAutomation = bytearray()
		for i in range(2):
			fanAutomation.append(raw[PROTOCOL_HEADER_SIZE + i])
		
		return fanAutomation

	

	# -----------------------------------------------------------
	# Function for setting battery max charge level
	# Parameter : uint8 level [%] 
	# Return : uint8 result [true, false]
	# -----------------------------------------------------------
	def setBatteryMaxChargeLevel(self, level):
		command.createSetCommand(command.PROTOCOL_COMMAND_SET_BATTERY_MAX_CHARGE_LEVEL, level, 1)
		command.sendCommand()
		delay_ms(RESPONSE_DELAY)
		raw = command.recieveCommand(COMMAND_SIZE_FOR_UINT8)

		level = raw[PROTOCOL_HEADER_SIZE]
		return level


	# -----------------------------------------------------------
	# Function for getting battery max charge level
	# Parameter : None
	# Return : int8 level [true, false]
	# -----------------------------------------------------------
	def getBatteryMaxChargeLevel(self):
		command.createCommand(command.PROTOCOL_COMMAND_GET_BATTERY_MAX_CHARGE_LEVEL)
		command.sendCommand()
		delay_ms(RESPONSE_DELAY)
		raw = command.recieveCommand(COMMAND_SIZE_FOR_UINT8)

		level = raw[PROTOCOL_HEADER_SIZE]
		return level

	
	# -----------------------------------------------------------
	# Function for setting safe shutdown battery level
	# Parameter : uint8 level [%] 
	# Return : uint8 result [true, false]
	# -----------------------------------------------------------
	def setSafeShutdownBatteryLevel(self, level):
		command.createSetCommand(command.PROTOCOL_COMMAND_SET_SAFE_SHUTDOWN_BATTERY_LEVEL, level, 1)
		command.sendCommand()
		delay_ms(RESPONSE_DELAY)
		raw = command.recieveCommand(COMMAND_SIZE_FOR_UINT8)

		level = raw[PROTOCOL_HEADER_SIZE]
		return level


	# -----------------------------------------------------------
	# Function for getting safe shutdown battery level
	# Parameter : None
	# Return : int8 level [true, false]
	# -----------------------------------------------------------
	def getSafeShutdownBatteryLevel(self):
		command.createCommand(command.PROTOCOL_COMMAND_GET_SAFE_SHUTDOWN_BATTERY_LEVEL)
		command.sendCommand()
		delay_ms(RESPONSE_DELAY)
		raw = command.recieveCommand(COMMAND_SIZE_FOR_UINT8)

		level = raw[PROTOCOL_HEADER_SIZE]
		return level


	# -----------------------------------------------------------
	# Function for setting safe shutdown status
	# Parameter : uint8 status [%] 
	# Return : uint8 result [true, false]
	# -----------------------------------------------------------
	def setSafeShutdownBatteryStatus(self, status):
		command.createSetCommand(command.PROTOCOL_COMMAND_SET_SAFE_SHUTDOWN_STATUS, status, 1)
		command.sendCommand()
		delay_ms(RESPONSE_DELAY)
		raw = command.recieveCommand(COMMAND_SIZE_FOR_UINT8)

		status = raw[PROTOCOL_HEADER_SIZE]
		return status


	# -----------------------------------------------------------
	# Function for setting safe shutdown status
	# Parameter : None
	# Return : int8 status [true, false]
	# -----------------------------------------------------------
	def getSafeShutdownBatteryStatus(self):
		command.createCommand(command.PROTOCOL_COMMAND_GET_SAFE_SHUTDOWN_STATUS)
		command.sendCommand()
		delay_ms(RESPONSE_DELAY)
		raw = command.recieveCommand(COMMAND_SIZE_FOR_UINT8)

		status = raw[PROTOCOL_HEADER_SIZE]
		return status


	# -----------------------------------------------------------
	# Function for getting working mode
	# Parameter : None
	# Return : int8 workingMode [charging, Fully Charged - Adapter Powered, Battery Powered ]
	# -----------------------------------------------------------
	def getWorkingMode(self):
		command.createCommand(command.PROTOCOL_COMMAND_GET_WORKING_MODE)
		command.sendCommand()
		delay_ms(RESPONSE_DELAY)
		raw = command.recieveCommand(COMMAND_SIZE_FOR_UINT8)

		mode = raw[PROTOCOL_HEADER_SIZE]
		return mode


	# -----------------------------------------------------------
	# Function for getting button 1
	# Parameter : None
	# Return : int8 buttonStatus [pressed, released]
	# -----------------------------------------------------------
	def getButton1Status(self):
		command.createCommand(command.PROTOCOL_COMMAND_GET_BUTTON1_STATUS)
		command.sendCommand()
		delay_ms(RESPONSE_DELAY)
		raw = command.recieveCommand(COMMAND_SIZE_FOR_UINT8)

		status = raw[PROTOCOL_HEADER_SIZE]
		return status


	# -----------------------------------------------------------
	# Function for getting button 2
	# Parameter : None
	# Return : int8 buttonStatus [pressed, released]
	# -----------------------------------------------------------
	def getButton2Status(self):
		command.createCommand(command.PROTOCOL_COMMAND_GET_BUTTON2_STATUS)
		command.sendCommand()
		delay_ms(RESPONSE_DELAY)
		raw = command.recieveCommand(COMMAND_SIZE_FOR_UINT8)

		status = raw[PROTOCOL_HEADER_SIZE]
		return status



	# -----------------------------------------------------------
	# Function for setting RTC Time
	# Parameter : uint64 timestamp [timestamp] 
	# Return : uint8 result [true, false]
	# -----------------------------------------------------------
	def setRtcTime(self, timestamp):
		command.createSetCommand(command.PROTOCOL_COMMAND_SET_RTC_TIME, timestamp, 4)
		command.sendCommand()
		delay_ms(RESPONSE_DELAY)
		raw = command.recieveCommand(COMMAND_SIZE_FOR_UINT8)

		result = raw[PROTOCOL_HEADER_SIZE]
		return result


	# -----------------------------------------------------------
	# Function for getting RTC Time
	# Parameter : format [Definition -> TIME_FORMAT_EPOCH, TIME_FORMAT_DATE_AND_TIME, TIME_FORMAT_DATE, TIME_FORMAT_TIME]
	# Return : uint32 timestamp | string date_and_time | string date | string time
	# -----------------------------------------------------------
	def getRtcTime(self, format = Definition.TIME_FORMAT_EPOCH):
		command.createCommand(command.PROTOCOL_COMMAND_GET_RTC_TIME)
		command.sendCommand()
		delay_ms(RESPONSE_DELAY)
		raw = command.recieveCommand(COMMAND_SIZE_FOR_INT32)

		timestamp = int.from_bytes(raw[PROTOCOL_HEADER_SIZE : COMMAND_SIZE_FOR_INT32 - 2], "big")

		if(format == Definition.TIME_FORMAT_EPOCH):
			return timestamp
		elif(format == Definition.TIME_FORMAT_DATE_AND_TIME):
			date_and_time = datetime.datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')
			return date_and_time
		elif(format == Definition.TIME_FORMAT_DATE):
			date = datetime.datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d')
			return date
		elif(format == Definition.TIME_FORMAT_TIME):
			time = datetime.datetime.fromtimestamp(timestamp).strftime('%H:%M:%S')
			return time


	# -----------------------------------------------------------
	# Function for hard powering off
	# Parameter : None 
	# Return : uint8 result [true, false]
	# -----------------------------------------------------------
	def hardPowerOff(self):
		command.createCommand(command.PROTOCOL_COMMAND_HARD_POWER_OFF)
		command.sendCommand()
		delay_ms(RESPONSE_DELAY)
		raw = command.recieveCommand(COMMAND_SIZE_FOR_UINT8)

		result = raw[PROTOCOL_HEADER_SIZE]
		return result

	# -----------------------------------------------------------
	# Function for soft powering off
	# Parameter : None 
	# Return : uint8 result [true, false]
	# -----------------------------------------------------------
	def softPowerOff(self):
		command.createCommand(command.PROTOCOL_COMMAND_SOFT_POWER_OFF)
		command.sendCommand()
		delay_ms(RESPONSE_DELAY)
		raw = command.recieveCommand(COMMAND_SIZE_FOR_UINT8)

		result = raw[PROTOCOL_HEADER_SIZE]
		return result

	
	# -----------------------------------------------------------
	# Function for hard rebooting
	# Parameter : None 
	# Return : uint8 result [true, false]
	# -----------------------------------------------------------
	def hardReboot(self):
		command.createCommand(command.PROTOCOL_COMMAND_HARD_REBOOT)
		command.sendCommand()
		delay_ms(RESPONSE_DELAY)
		raw = command.recieveCommand(COMMAND_SIZE_FOR_UINT8)

		result = raw[PROTOCOL_HEADER_SIZE]
		return result


	# -----------------------------------------------------------
	# Function for soft rebooting
	# Parameter : None 
	# Return : uint8 result [true, false]
	# -----------------------------------------------------------
	def softReboot(self):
		command.createCommand(command.PROTOCOL_COMMAND_SOFT_REBOOT)
		command.sendCommand()
		delay_ms(RESPONSE_DELAY)
		raw = command.recieveCommand(COMMAND_SIZE_FOR_UINT8)

		result = raw[PROTOCOL_HEADER_SIZE]
		return result


	# -----------------------------------------------------------
	# Function for asking watchdog alarm exist
	# Parameter : None 
	# Return : uint8 alarm [true, false]
	# -----------------------------------------------------------
	def askWatchdogAlarm(self):
		command.createCommand(command.PROTOCOL_COMAMND_WATCHDOG_ALARM)
		command.sendCommand()
		delay_ms(RESPONSE_DELAY)
		raw = command.recieveCommand(COMMAND_SIZE_FOR_INT16)

		alarm_status = int.from_bytes(raw[PROTOCOL_HEADER_SIZE : COMMAND_SIZE_FOR_INT16 - 2 ], "big")
		return alarm_status

	# -----------------------------------------------------------
	# Function for getting battery design capacity
	# Parameter : None 
	# Return : uint16 capacity [maH]
	# -----------------------------------------------------------
	def getBatteryDesignCapacity(self):
		command.createCommand(command.PROTOCOL_COMMAND_GET_BATTERY_DESIGN_CAPACITY)
		command.sendCommand()
		delay_ms(RESPONSE_DELAY)
		raw = command.recieveCommand(COMMAND_SIZE_FOR_INT16)

		capacity = int.from_bytes(raw[PROTOCOL_HEADER_SIZE : COMMAND_SIZE_FOR_INT16 - 2 ], "big")
		return capacity


	# -----------------------------------------------------------
	# Function for setting battery design capacity
	# Parameter : int16 cap [maH] 
	# Return : uint8 result [true, false]
	# -----------------------------------------------------------
	def setBatteryDesignCapacity(self, capacity):
		command.createSetCommand(command.PROTOCOL_COMMAND_SET_BATTERY_DESIGN_CAPACITY, capacity, 2)
		command.sendCommand()
		delay_ms(RESPONSE_DELAY)
		raw = command.recieveCommand(COMMAND_SIZE_FOR_UINT8)

		status = raw[PROTOCOL_HEADER_SIZE]
		return status


	# -----------------------------------------------------------
	# Function for creating scheduling event
	# Parameter : uint8 eventID [id]
	# Parameter : uint8 scheduleType [time, interval]
	# Parameter : uint8 repeat [once, repeated]
	# Parameter : uint32 timeOrInterval [exact time[epoch], interval]
	# Parameter : uint8 interval_type [seconds, minutes, hours, days]
	# Parameter : uint8 repeatPeriod [day_factor]  
	#########################################################################################################								 
	# [monday] - [tuesday] - [wednesday] - [thursday] - [friday] - [saturday] - [sunday] - [RESERVED as Zero]
	# Bit 0		 Bit 1	     Bit 2	       Bit 3		Bit 4	   Bit 5		Bit 6	   Bit 7
	#								 			
	# *** Example Calculation for every day ***
	# day_factor = 0b01111111 = 127
	#
	# *** Example Calculation for (sunday+monday+tuesday) ***
	# day_factor = 0b01000011 = 67
	######################################################################################################### 	
	# Parameter : uint8 action [start, hard shutdown, soft shutdown, hard reboot, soft reboot]
	# Return : result
	# -----------------------------------------------------------
	def createScheduledEvent(self, eventID, scheduleType, repeat, timeOrInterval, interval_type, repeatPeriod, action):

		value = bytearray()
		value.append(eventID)
		value.append(scheduleType)
		value.append(repeat)
		value.append((timeOrInterval >> 24) & 0xFF)
		value.append((timeOrInterval >> 16) & 0xFF)
		value.append((timeOrInterval >> 8) & 0xFF)
		value.append(timeOrInterval & 0xFF)
		value.append(interval_type)
		value.append(repeatPeriod)
		value.append(action)

		command.createSetCommand(command.PROTOCOL_COMMAND_CREATE_SCHEDULED_EVENT, value, 10)
		command.sendCommand()
		delay_ms(RESPONSE_DELAY)
		raw = command.recieveCommand(COMMAND_SIZE_FOR_UINT8)

		result = raw[PROTOCOL_HEADER_SIZE]
		return result


	# -----------------------------------------------------------
	# Function for removing scheduling event
	# Parameter : uint8 eventID [celcius]
	# Return : result
	# -----------------------------------------------------------
	def removeScheduledEvent(self, eventID):

		command.createSetCommand(command.PROTOCOL_COMMAND_REMOVE_SCHEDULED_EVENT, eventID, 1)
		command.sendCommand()
		delay_ms(RESPONSE_DELAY)
		raw = command.recieveCommand(COMMAND_SIZE_FOR_UINT8)

		result = raw[PROTOCOL_HEADER_SIZE]
		return result
	
	# -----------------------------------------------------------
	# Function for removing scheduling event
	# Return : result
	# -----------------------------------------------------------
	def removeAllScheduledEvents(self):

		command.createCommand(command.PROTOCOL_COMMAND_REMOVE_ALL_SCHEDULED_EVENTS)
		command.sendCommand()
		delay_ms(RESPONSE_DELAY)
		raw = command.recieveCommand(COMMAND_SIZE_FOR_UINT8)

		result = raw[PROTOCOL_HEADER_SIZE]
		return result

	
	# -----------------------------------------------------------
	# Function for getting firmware ver
	# Parameter : None
	# Return : char[8] ver [Ex. v1.00.00]
	# -----------------------------------------------------------
	def getFirmwareVer(self):
		command.createCommand(command.PROTOCOL_COMMAND_GET_FIRMWARE_VER)
		command.sendCommand()
		delay_ms(RESPONSE_DELAY)
		raw = command.recieveCommand(15)
		ver = bytearray(8)
		
		for i in range(8):
			ver[i] = raw[PROTOCOL_HEADER_SIZE + i ]
		
		return ver

