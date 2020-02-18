#!/usr/bin/python3

import smbus2
import RPi.GPIO as GPIO
import time
from crc16 import CRC16
import struct

bus = smbus2.SMBus(1)
crc = CRC16();

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


COMMAND_TYPE_REQUEST = 				0x01
COMMAND_TYPE_RESPONSE = 			0x02
COMMAND_TYPE_RESPONSE =				0x03

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
PROTOCOL_COMMAND_GET_BATTERY_PERCENTAGE = 				13
PROTOCOL_COMMAND_GET_BATTERY_HEALT =	 				14
PROTOCOL_COMMAND_GET_FAN_SPEED = 						15
PROTOCOL_COMMAND_GET_WATCHDOG_STATUS = 					16
PROTOCOL_COMMAND_GET_BATTERY_CHARGE_MAX_PERCENTAGE = 	17



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
		print(bufferSend)
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
			return bufferRecieve[0:PROTOCOL_FRAME_SIZE + datalen]

			bufferRecieveIndex = 0


	def recieveCommand(self, lenOfResponse):
		global bufferRecieve
			
		for i in range(lenOfResponse):
			c = bus.read_byte(DEVICE_ADDRESS)
			print("Recieved byte: " + str(hex(c)))
			msg = self.checkCommand(c)
			
			if(msg != None and msg != -1):
				return msg


	def createCommand(self, command, command_type = COMMAND_TYPE_REQUEST):
		global bufferSend
		bufferSend.append(START_BYTE_SENT)
		bufferSend.append(command)
		bufferSend.append(COMMAND_TYPE_REQUEST)
		bufferSend.append(0x00)
		bufferSend.append(0x00)
		(crcHigh, crcLow) = self.calculateCRC16(bufferSend[0:PROTOCOL_HEADER_SIZE])
		bufferSend.append(crcHigh)
		bufferSend.append(crcLow)

	def calculateCRC16(self, command, returnType = 0):
		datalen = (command[3] << 8) + (command[4] & 0xFF)
		command = command[0 : PROTOCOL_HEADER_SIZE + datalen]
		print("calculateCRC Func: " + str(command))

		calCRC = crc.exampleOfUseCRC16(bytes(command), PROTOCOL_HEADER_SIZE + datalen)
		crcHigh = (calCRC >> 8) & 0xFF
		crcLow = calCRC & 0xFF
		print("CRC16: " + str(calCRC) + "\rCRC16 High: " + str(crcHigh) + "\rCRC16 Low: " + str(crcLow))
		
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
		self.createCommand(PROTOCOL_COMMAND_GET_SYSTEM_POWER)
		self.sendCommand()
		delay_ms(RESPONSE_DELAY)
		raw = self.recieveCommand(COMMAND_SIZE_FOR_INT32)

		power = int.from_bytes(raw[PROTOCOL_HEADER_SIZE : COMMAND_SIZE_FOR_INT32 - 2 ], "big")
		return power / 100


# Example Code Area

pms = SixfabPMS()

print(pms.getInputTemp())

# End of Example Code Area	

	
