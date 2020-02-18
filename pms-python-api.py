#!/usr/bin/python3

import smbus2
import RPi.GPIO as GPIO
import time
from crc16 import crc16

bus = smbus2.SMBus(1)
crc = crc16.CRC16();

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

COMMAND_TYPE_REQUEST = 				0x01
COMMAND_TYPE_RESPONSE = 			0x02
COMMAND_TYPE_RESPONSE =				0x03

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
def delay(ms):
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
		self.clearGPIOs()
			
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
			return
			
		bufferRecieve.append(recievedByte)
		bufferRecieveIndex += 1
		
		if(bufferRecieveIndex < PROTOCOL_HEADER_SIZE):
			return
		
		datalen = (bufferRecieve[3] << 8) | bufferRecieve[4]
		datalen = datalen / 2

		if(bufferRecieveIndex == (PROTOCOL_FRAME_SIZE + datalen)):
			print('[{}]'.format(', '.join(hex(x) for x in bufferRecieve)))
			bufferRecieveIndex = 0
		
		
	def recieveCommand(self, lenOfResponse):
		global bufferRecieve
			
		for i in range(lenOfResponse):
			c = bus.read_byte(DEVICE_ADDRESS)
			print("Recieved byte: " + str(hex(c)))
			self.checkCommand(c)

	def createDummyData(self, command):
		global bufferSend
		bufferSend.append(START_BYTE_SENT)
		bufferSend.append(command)
		bufferSend.append(COMMAND_TYPE_REQUEST)
		bufferSend.append(0x00)
		bufferSend.append(0x00)


	def calculateCRC16(self, command):
		datalen = (command[3] << 8) + (command[4] & 0xFF)
		command = command[0 : PROTOCOL_HEADER_SIZE + datalen]
		print(command)

		calCRC = crc.exampleOfUseCRC16(bytes(command), PROTOCOL_HEADER_SIZE + datalen)
		print(calCRC)
		crcHigh = (calCRC >> 8) & 0xFF
		crcLow = calCRC & 0xFF
		print(crcHigh)
		print(crcLow)
		bufferSend.append(crcHigh)
		bufferSend.append(crcLow)
		

# Example Code Area

pms = SixfabPMS()

pms.createDummyData(1)
pms.calculateCRC16(bufferSend)
pms.sendCommand()
time.sleep(0.1)
pms.recieveCommand(16)
# End of Example Code Area	

	
