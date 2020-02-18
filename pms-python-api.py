#!/usr/bin/python3

import smbus2
import time

bus = smbus2.SMBus(1)

bufferRecieveIndex = 0

#############################################################
### Communication Protocol ##################################
#############################################################
bufferSend = list()
bufferRecieve = list()
buff = list()

START_BYTE_RECIEVED = 				0xDC 		# Start Byte
START_BYTE_SENDED = 				0xCD 		# Start Byte
PROTOCOL_HEADER_SIZE =			5
PROTOCOL_FRAME_SIZE =			7

COMMAND_TYPE_REQUEST = 		0x01
COMMAND_TYPE_RESPONSE = 	0x02
COMMAND_TYPE_RESPONSE =		0x03

DEVICE_ADDRESS = 0x41      #7 bit address (will be left shifted to add the read write bit)

#############################################################
### Public Functions ########################################
#############################################################
def sendCommand():
	global bufferSend
	print(bufferSend)
	bus.write_i2c_block_data(DEVICE_ADDRESS, 0x01, bufferSend)

def checkCommand(recievedByte):
	global bufferRecieve
	global bufferRecieveIndex
	datalen = 0

	if(bufferRecieveIndex == 0 and recievedByte != START_BYTE_RECIEVED):
		return
	
	#print("START BYTE\n")
	
	bufferRecieve.append(recievedByte)
	bufferRecieveIndex += 1
	
	if(bufferRecieveIndex < PROTOCOL_HEADER_SIZE):
		return
	
	#print("HEADER\n")
	
	#print( "START_BYTE:	" + hex(bufferRecieve[0]) + "\n" )
	#print( "COMMAND:	" + hex(bufferRecieve[1]) + "\n" )
	#print( "COMMAND_TYPE:	" + hex(bufferRecieve[2]) + "\n" )
	#print( "DATALEN[HIGH]:	" + hex(bufferRecieve[3]) + "\n" )
	#print( "DATALEN[LOW]:	" + hex(bufferRecieve[4]) + "\n" )
	
	
	datalen = (bufferRecieve[3] << 8) | bufferRecieve[4]
	
	#print("DATALEN" + str(datalen) + "\r\n")
	#print('[{}]'.format(', '.join(hex(x) for x in bufferRecieve)))
	
	if(bufferRecieveIndex == (PROTOCOL_FRAME_SIZE + datalen/2)):
		print('[{}]'.format(', '.join(hex(x) for x in bufferRecieve)))
		bufferRecieveIndex = 0
	
	
def recieveCommand(lenOfResponse):
	global bufferRecieve
	global bufferRecieveIndex
	
	#bufferRecieve = bus.read_i2c_block_data(0x41,0xCD,PROTOCOL_FRAME_SIZE+5)
	#print('[{}]'.format(', '.join(hex(x) for x in bufferRecieve)))
	
	for i in range(lenOfResponse):
		c = bus.read_byte(DEVICE_ADDRESS)
		print("Recieved byte: " + str(hex(c)))
		checkCommand(c)

def createDummyData(command):
	global bufferSend
	bufferSend.append(START_BYTE_SENDED)
	bufferSend.append(command)
	bufferSend.append(COMMAND_TYPE_REQUEST)
	bufferSend.append(0x00)
	bufferSend.append(0x00)
	bufferSend.append(0x05)
	bufferSend.append(0x04)

# Example Code Area

createDummyData(1)
sendCommand()
time.sleep(0.1)
recieveCommand(16)

# End of Example Code Area	

	
