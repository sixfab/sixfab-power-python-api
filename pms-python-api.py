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

START_BYTE_RECIEVED = 				0xDC 		# Start Byte Recieved
START_BYTE_SENT = 					0xCD 		# Start Byte Sent
PROTOCOL_HEADER_SIZE =				5
PROTOCOL_FRAME_SIZE =				7
COMMAND_SIZE_FOR_FLOAT = 			11
COMMAND_SIZE_FOR_DOUBLE = 			13
COMMAND_SIZE_FOR_INT = 				9
COMMAND_SIZE_FOR_INT32 = 			11


COMMAND_TYPE_REQUEST = 				0x01
COMMAND_TYPE_RESPONSE = 			0x02
COMMAND_TYPE_RESPONSE =				0x03

DEVICE_ADDRESS = 0x41      #7 bit address (will be left shifted to add the read write bit)

PROTOCOL_COMMAND_GET_INPUT_TEMP = 				1
PROTOCOL_COMMAND_GET_INPUT_VOLTAGE = 			2
PROTOCOL_COMMAND_GET_INPUT_CURRENT = 			3
PROTOCOL_COMMAND_GET_INPUT_POWER =	 			4

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

	def calculateCRC16(self, command):
		datalen = (command[3] << 8) + (command[4] & 0xFF)
		command = command[0 : PROTOCOL_HEADER_SIZE + datalen]
		print("calculateCRC Func: " + str(command))

		calCRC = crc.exampleOfUseCRC16(bytes(command), PROTOCOL_HEADER_SIZE + datalen)
		print(calCRC)
		crcHigh = (calCRC >> 8) & 0xFF
		crcLow = calCRC & 0xFF
		print(crcHigh)
		print(crcLow)
		return (crcHigh, crcLow)
		

	def getInputTemp(self):
		self.createCommand(PROTOCOL_COMMAND_GET_INPUT_TEMP)
		self.sendCommand()
		delay_ms(100)
		raw = self.recieveCommand(COMMAND_SIZE_FOR_FLOAT)

		temp = int.from_bytes(raw[PROTOCOL_HEADER_SIZE:9], "big")
		return temp / 100



# Example Code Area

pms = SixfabPMS()

print(pms.getInputTemp())

# End of Example Code Area	

	
