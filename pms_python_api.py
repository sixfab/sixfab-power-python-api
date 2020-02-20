#!/usr/bin/python3

import smbus2
import RPi.GPIO as GPIO
import time
from crc16 import CRC16
import struct

bus = smbus2.SMBus(1)
crc = CRC16()

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


COMMAND_TYPE_REQUEST = 				0x01
COMMAND_TYPE_RESPONSE = 			0x02

DEVICE_ADDRESS = 0x41      #7 bit address (will be left shifted to add the read write bit)

PROTOCOL_COMMAND_GET_INPUT_TEMP = 						1
PROTOCOL_COMMAND_GET_INPUT_VOLTAGE = 					2
PROTOCOL_COMMAND_GET_INPUT_CURRENT = 					3
PROTOCOL_COMMAND_GET_INPUT_POWER =	 					4
PROTOCOL_COMMAND_GET_SYSTEM_TEMP = 						5
PROTOCOL_COMMAND_GET_SYSTEM_VOLTAGE = 					6
PROTOCOL_COMMAND_GET_SYSTEM_CURRENT = 					7
PROTOCOL_COMMAND_GET_SYSTEM_POWER =	 					8
PROTOCOL_COMMAND_GET_BATTERY_TEMP = 					9
PROTOCOL_COMMAND_GET_BATTERY_VOLTAGE = 					10
PROTOCOL_COMMAND_GET_BATTERY_CURRENT = 					11
PROTOCOL_COMMAND_GET_BATTERY_POWER =	 				12
PROTOCOL_COMMAND_GET_BATTERY_LEVEL = 					13
PROTOCOL_COMMAND_GET_BATTERY_HEALT =	 				14
PROTOCOL_COMMAND_GET_FAN_SPEED = 						15
PROTOCOL_COMMAND_GET_WATCHDOG_STATUS = 					16
PROTOCOL_COMMAND_SET_WATCHDOG_STATUS =  				17
PROTOCOL_COMMAND_SET_RGB_ANIMATION = 					18
PROTOCOL_COMMAND_GET_RGB_ANIMATION = 					19
PROTOCOL_COMMAND_SET_FAN_SPEED = 						20
PROTOCOL_COMMAND_SET_FAN_AUTOMATION = 					21
PROTOCOL_COMMAND_GET_FAN_AUTOMATION = 					22
# -----------------------------------------------------	23
PROTOCOL_COMMAND_SET_BATTERY_MAX_CHARGE_LEVEL = 		24
PROTOCOL_COMMAND_GET_BATTERY_MAX_CHARGE_LEVEL = 		25
PROTOCOL_COMMAND_SET_SAFE_SHUTDOWN_BATTERY_LEVEL = 		26
PROTOCOL_COMMAND_GET_SAFE_SHUTDOWN_BATTERY_LEVEL = 		27
PROTOCOL_COMMAND_SET_SAFE_SHUTDOWN_STATUS = 			28
PROTOCOL_COMMAND_GET_SAFE_SHUTDOWN_STATUS = 			29
PROTOCOL_COMMAND_GET_POWER_MODE = 						30
PROTOCOL_COMMAND_GET_BUTTON1_STATUS = 					31
PROTOCOL_COMMAND_GET_BUTTON2_STATUS = 					32
PROTOCOL_COMMAND_SET_RTC_TIME = 						33
PROTOCOL_COMMAND_GET_RTC_TIME =		 					34
PROTOCOL_COMMAND_HARD_POWER_OFF =		 				35
PROTOCOL_COMMAND_SOFT_POWER_OFF =		 				36
PROTOCOL_COMMAND_HARD_REBOOT =			 				37
PROTOCOL_COMMAND_SOFT_REBOOT =		 					38
# .
# .
# .
PROTOCOL_COMMAND_CREATE_SCHEDULED_EVENT = 				100
PROTOCOL_COMMAND_REMOVE_SCHEDULED_EVENT = 				101
PROTOCOL_COMMAND_EDIT_SCHEDULED_EVENT = 				102
# .
# .
# .
PROTOCOL_COMMAND_GET_FIRMWARE_VER =	 					200





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
		#self.clearGPIOs()
		print("Class Destructed")
			

	# Function for clearing GPIO's setup
	def clearGPIOs(self):
		GPIO.cleanup()


	#############################################################
	### I2C Protocol Functions ##################################
	#############################################################
	def sendCommand(self):
		global bufferSend
		print("Sent Command:")
		print('[{}]'.format(', '.join(hex(x) for x in bufferSend)))
		bus.write_i2c_block_data(DEVICE_ADDRESS, 0x01, bufferSend)
		

	def checkCommand(self, recievedByte):
		global bufferRecieve
		global bufferRecieveIndex
		datalen = 0

		if(bufferRecieveIndex == 0 and recievedByte != START_BYTE_RECIEVED):
			return -1
			
		bufferRecieve.append(recievedByte)
		bufferRecieveIndex += 1
		
		if(bufferRecieveIndex < PROTOCOL_HEADER_SIZE):
			return -1
		
		datalen = (bufferRecieve[3] << 8) | bufferRecieve[4]
		datalen = int(datalen / 2)

		if(bufferRecieveIndex == (PROTOCOL_FRAME_SIZE + datalen)):
			crcRecieved = (bufferRecieve[PROTOCOL_FRAME_SIZE + datalen -2] << 8) | bufferRecieve[PROTOCOL_FRAME_SIZE + datalen - 1]

			print("CRC Check ABORT!")
			print('[{}]'.format(', '.join(hex(x) for x in bufferRecieve)))
			bufferRecieveIndex = 0
			return bufferRecieve[0:PROTOCOL_FRAME_SIZE + datalen]


	def recieveCommand(self, lenOfResponse):
		global bufferRecieve
			
		for i in range(lenOfResponse):
			c = bus.read_byte(DEVICE_ADDRESS)
			#print("Recieved byte: " + str(hex(c)))
			msg = self.checkCommand(c)
			
			if(msg != None and msg != -1):
				bufferRecieve.clear()
				return msg


	def createCommand(self, command, command_type = COMMAND_TYPE_REQUEST):
		global bufferSend
		bufferSend.clear()
		bufferSend.append(START_BYTE_SENT)
		bufferSend.append(command)
		bufferSend.append(command_type)
		bufferSend.append(0x00)
		bufferSend.append(0x00)
		(crcHigh, crcLow) = self.calculateCRC16(bufferSend[0:PROTOCOL_HEADER_SIZE])
		bufferSend.append(crcHigh)
		bufferSend.append(crcLow)


	def createSetCommand(self, command, value, lenByte, command_type = COMMAND_TYPE_REQUEST):
		global bufferSend
		bufferSend.clear()
		bufferSend.append(START_BYTE_SENT)
		bufferSend.append(command)
		bufferSend.append(command_type)

		lenLow = lenByte & 0xFF
		lenHigh = (lenByte >> 8) & 0xFF

		bufferSend.append(lenHigh)
		bufferSend.append(lenLow)

		byteArray = value.to_bytes(len(value),"big")
		bufferSend.append(byteArray)
		print(bufferSend)

		(crcHigh, crcLow) = self.calculateCRC16(bufferSend[0:PROTOCOL_HEADER_SIZE+lenByte])
		bufferSend.append(crcHigh)
		bufferSend.append(crcLow)
		print(bufferSend)

	def calculateCRC16(self, command, returnType = 0):
		datalen = (command[3] << 8) + (command[4] & 0xFF)
		command = command[0 : PROTOCOL_HEADER_SIZE + datalen]
		#print("calculateCRC Func: " + str(command))

		calCRC = crc.exampleOfUseCRC16(bytes(command), PROTOCOL_HEADER_SIZE + datalen)
		crcHigh = (calCRC >> 8) & 0xFF
		crcLow = calCRC & 0xFF
		print("CRC16: " + str(calCRC) + "\t" + "CRC16 High: " + str(crcHigh) + "\t" + "CRC16 Low: " + str(crcLow))
		
		if(returnType == 0):
			return (crcHigh, crcLow)
		else:
			return calCRC
		

	#############################################################
	### API Call Methods ########################################
	#############################################################
	
	# -----------------------------------------------------------
	# Function for getting input temperature
	# Parameter : None
	# Return : float temp [Celcius]
	# -----------------------------------------------------------
	def getInputTemp(self):
		self.createCommand(PROTOCOL_COMMAND_GET_INPUT_TEMP)
		self.sendCommand()
		delay_ms(RESPONSE_DELAY)
		raw = self.recieveCommand(COMMAND_SIZE_FOR_INT32)

		temp = int.from_bytes(raw[PROTOCOL_HEADER_SIZE:COMMAND_SIZE_FOR_INT32 - 2], "big")
		return temp / 100


	# -----------------------------------------------------------
	# Function for getting input voltage
	# Parameter : None
	# Return : float voltage [Volt]
	# -----------------------------------------------------------
	def getInputVoltage(self):
		self.createCommand(PROTOCOL_COMMAND_GET_INPUT_VOLTAGE)
		self.sendCommand()
		delay_ms(RESPONSE_DELAY)
		raw = self.recieveCommand(COMMAND_SIZE_FOR_INT32)

		voltage = int.from_bytes(raw[PROTOCOL_HEADER_SIZE : COMMAND_SIZE_FOR_INT32 - 2 ], "big")
		return voltage / 100


	# -----------------------------------------------------------
	# Function for getting input current
	# Parameter : None
	# Return : float current [Ampere]
	# -----------------------------------------------------------
	def getInputCurrent(self):
		self.createCommand(PROTOCOL_COMMAND_GET_INPUT_CURRENT)
		self.sendCommand()
		delay_ms(RESPONSE_DELAY)
		raw = self.recieveCommand(COMMAND_SIZE_FOR_INT32)

		current = int.from_bytes(raw[PROTOCOL_HEADER_SIZE : COMMAND_SIZE_FOR_INT32 - 2 ], "big")
		return current / 100


	# -----------------------------------------------------------
	# Function for getting input power
	# Parameter : None
	# Return : float power [Watt]
	# -----------------------------------------------------------
	def getInputPower(self):
		self.createCommand(PROTOCOL_COMMAND_GET_INPUT_POWER)
		self.sendCommand()
		delay_ms(RESPONSE_DELAY)
		raw = self.recieveCommand(COMMAND_SIZE_FOR_INT32)

		power = int.from_bytes(raw[PROTOCOL_HEADER_SIZE : COMMAND_SIZE_FOR_INT32 - 2 ], "big")
		return power / 100


	# -----------------------------------------------------------
	# Function for getting system temperature
	# Parameter : None
	# Return : float temp [Celcius]
	# -----------------------------------------------------------
	def getSystemTemp(self):
		self.createCommand(PROTOCOL_COMMAND_GET_SYSTEM_TEMP)
		self.sendCommand()
		delay_ms(RESPONSE_DELAY)
		raw = self.recieveCommand(COMMAND_SIZE_FOR_INT32)

		temp = int.from_bytes(raw[PROTOCOL_HEADER_SIZE:COMMAND_SIZE_FOR_INT32 - 2], "big")
		return temp / 100


	# -----------------------------------------------------------
	# Function for getting system voltage
	# Parameter : None
	# Return : float voltage [Volt]
	# -----------------------------------------------------------
	def getSystemVoltage(self):
		self.createCommand(PROTOCOL_COMMAND_GET_SYSTEM_VOLTAGE)
		self.sendCommand()
		delay_ms(RESPONSE_DELAY)
		raw = self.recieveCommand(COMMAND_SIZE_FOR_INT32)

		voltage = int.from_bytes(raw[PROTOCOL_HEADER_SIZE : COMMAND_SIZE_FOR_INT32 - 2 ], "big")
		return voltage / 100


	# -----------------------------------------------------------
	# Function for getting system current
	# Parameter : None
	# Return : float current [Ampere]
	# -----------------------------------------------------------
	def getSystemCurrent(self):
		self.createCommand(PROTOCOL_COMMAND_GET_SYSTEM_CURRENT)
		self.sendCommand()
		delay_ms(RESPONSE_DELAY)
		raw = self.recieveCommand(COMMAND_SIZE_FOR_INT32)

		current = int.from_bytes(raw[PROTOCOL_HEADER_SIZE : COMMAND_SIZE_FOR_INT32 - 2 ], "big")
		return current / 100


	# -----------------------------------------------------------
	# Function for getting system power
	# Parameter : None
	# Return : float power [Watt]
	# -----------------------------------------------------------
	def getSystemPower(self):
		self.createCommand(PROTOCOL_COMMAND_GET_SYSTEM_POWER)
		self.sendCommand()
		delay_ms(RESPONSE_DELAY)
		raw = self.recieveCommand(COMMAND_SIZE_FOR_INT32)

		power = int.from_bytes(raw[PROTOCOL_HEADER_SIZE : COMMAND_SIZE_FOR_INT32 - 2 ], "big")
		return power / 100


	# -----------------------------------------------------------
	# Function for getting battery temperature
	# Parameter : None
	# Return : float temp [Celcius]
	# -----------------------------------------------------------
	def getBatteryTemp(self):
		self.createCommand(PROTOCOL_COMMAND_GET_BATTERY_TEMP)
		self.sendCommand()
		delay_ms(RESPONSE_DELAY)
		raw = self.recieveCommand(COMMAND_SIZE_FOR_INT32)

		temp = int.from_bytes(raw[PROTOCOL_HEADER_SIZE:COMMAND_SIZE_FOR_INT32 - 2], "big")
		return temp / 100


	# -----------------------------------------------------------
	# Function for getting battery voltage
	# Parameter : None
	# Return : float voltage [Volt]
	# -----------------------------------------------------------
	def getBatteryVoltage(self):
		self.createCommand(PROTOCOL_COMMAND_GET_BATTERY_VOLTAGE)
		self.sendCommand()
		delay_ms(RESPONSE_DELAY)
		raw = self.recieveCommand(COMMAND_SIZE_FOR_INT32)

		voltage = int.from_bytes(raw[PROTOCOL_HEADER_SIZE : COMMAND_SIZE_FOR_INT32 - 2 ], "big")
		return voltage / 100


	# -----------------------------------------------------------
	# Function for getting battery current
	# Parameter : None
	# Return : float current [Ampere]
	# -----------------------------------------------------------
	def getBatteryCurrent(self):
		self.createCommand(PROTOCOL_COMMAND_GET_BATTERY_CURRENT)
		self.sendCommand()
		delay_ms(RESPONSE_DELAY)
		raw = self.recieveCommand(COMMAND_SIZE_FOR_INT32)

		current = int.from_bytes(raw[PROTOCOL_HEADER_SIZE : COMMAND_SIZE_FOR_INT32 - 2 ], "big")
		return current / 100


	# -----------------------------------------------------------
	# Function for getting battery power
	# Parameter : None
	# Return : float power [Watt]
	# -----------------------------------------------------------
	def getBatteryPower(self):
		self.createCommand(PROTOCOL_COMMAND_GET_BATTERY_POWER)
		self.sendCommand()
		delay_ms(RESPONSE_DELAY)
		raw = self.recieveCommand(COMMAND_SIZE_FOR_INT32)

		power = int.from_bytes(raw[PROTOCOL_HEADER_SIZE : COMMAND_SIZE_FOR_INT32 - 2 ], "big")
		return power / 100


	# -----------------------------------------------------------
	# Function for getting battery level
	# Parameter : None
	# Return : int level [%]
	# -----------------------------------------------------------
	def getBatteryLevel(self):
		self.createCommand(PROTOCOL_COMMAND_GET_BATTERY_LEVEL)
		self.sendCommand()
		delay_ms(RESPONSE_DELAY)
		raw = self.recieveCommand(COMMAND_SIZE_FOR_INT16)

		level = int.from_bytes(raw[PROTOCOL_HEADER_SIZE : COMMAND_SIZE_FOR_INT16 - 2 ], "big")
		return level


	# -----------------------------------------------------------
	# Function for getting battery healt
	# Parameter : None
	# Return : int healt [%]
	# -----------------------------------------------------------
	def getBatteryHealt(self):
		self.createCommand(PROTOCOL_COMMAND_GET_BATTERY_HEALT)
		self.sendCommand()
		delay_ms(RESPONSE_DELAY)
		raw = self.recieveCommand(COMMAND_SIZE_FOR_INT16)

		healt = int.from_bytes(raw[PROTOCOL_HEADER_SIZE : COMMAND_SIZE_FOR_INT16 - 2 ], "big")
		return healt


	# -----------------------------------------------------------
	# Function for getting fan speed
	# Parameter : None
	# Return : int speed [RPM]
	# -----------------------------------------------------------
	def getFanSpeed(self):
		self.createCommand(PROTOCOL_COMMAND_GET_FAN_SPEED)
		self.sendCommand()
		delay_ms(RESPONSE_DELAY)
		raw = self.recieveCommand(COMMAND_SIZE_FOR_INT16)

		rpm = int.from_bytes(raw[PROTOCOL_HEADER_SIZE : COMMAND_SIZE_FOR_INT16 - 2 ], "big")
		return rpm


	# -----------------------------------------------------------
	# Function for setting watchdog status
	# Parameter : uint8 status [true, false] 
	# Return : uint8 result [true, false]
	# -----------------------------------------------------------
	def setFanSpeed(self, status):
		self.createSetCommand(PROTOCOL_COMMAND_SET_FAN_SPEED, status, 1)
		self.sendCommand()
		delay_ms(RESPONSE_DELAY)
		raw = self.recieveCommand(COMMAND_SIZE_FOR_UINT8)

		result = raw[PROTOCOL_HEADER_SIZE + 1 ]
		return result


	# -----------------------------------------------------------
	# Function for getting watchdog status
	# Parameter : None
	# Return : int8 status [true, false]
	# -----------------------------------------------------------
	def getWatchdogStatus(self):
		self.createCommand(PROTOCOL_COMMAND_GET_WATCHDOG_STATUS)
		self.sendCommand()
		delay_ms(RESPONSE_DELAY)
		raw = self.recieveCommand(COMMAND_SIZE_FOR_UINT8)

		status = raw[PROTOCOL_HEADER_SIZE + 1]
		return status


	# -----------------------------------------------------------
	# Function for setting RGB animation
	# Parameter : uint8 type [DISABLED, HEARTBEAT, TEMP_MAP]
	# Parameter : uint8 color [RED, GREEN, BLUE, YELLOW, CYAN, MAGENTA, WHITE]
	# Parameter : uint8 speed [SLOW, NORMAL, FAST] 
	# Return : uint8 result [true, false]
	# -----------------------------------------------------------
	def setRgbAnimation(self, animType, color, speed):
		
		value = bytearray()
		value.append(bytes(animType))
		value.append(bytes(color))
		value.append(bytes(speed))

		self.createSetCommand(PROTOCOL_COMMAND_SET_RGB_ANIMATION, value, 3)
		self.sendCommand()
		delay_ms(RESPONSE_DELAY)
		raw = self.recieveCommand(COMMAND_SIZE_FOR_UINT8)

		result = raw[PROTOCOL_HEADER_SIZE + 1 ]
		return result



	# -----------------------------------------------------------
	# Function for getting RGB animation
	# Parameter : None
	# Return : byteArray(3) - ledAnimation[animType, color, speed]
	# -----------------------------------------------------------
	def getRgbAnimation(self):
		self.createCommand(PROTOCOL_COMMAND_GET_RGB_ANIMATION)
		self.sendCommand()
		delay_ms(RESPONSE_DELAY)
		raw = self.recieveCommand(10)

		animation = raw[PROTOCOL_HEADER_SIZE : 3]
		return animation


