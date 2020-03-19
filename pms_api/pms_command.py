#!/usr/bin/python3

import smbus2
import time
import struct
import crc16

bus = smbus2.SMBus(1)

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
COMMAND_SIZE_FOR_INT16 = 			9
COMMAND_SIZE_FOR_INT32 = 			11
COMMAND_SIZE_FOR_UINT8 = 			8
COMMAND_SIZE_FOR_INT64 = 			15

COMMAND_TYPE_REQUEST = 				0x01
COMMAND_TYPE_RESPONSE = 			0x02

DEVICE_ADDRESS =                    0x41        #7 bit address (will be left shifted to add the read write bit)

class Command:

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
    PROTOCOL_COMMAND_GET_BATTERY_HEALTH =	 				14
    PROTOCOL_COMMAND_GET_FAN_SPEED = 						15
    PROTOCOL_COMMAND_GET_WATCHDOG_STATUS = 					16
    PROTOCOL_COMMAND_SET_WATCHDOG_STATUS =  				17
    PROTOCOL_COMMAND_SET_RGB_ANIMATION = 					18
    PROTOCOL_COMMAND_GET_RGB_ANIMATION = 					19
    PROTOCOL_COMMAND_SET_FAN_SPEED = 						20
    PROTOCOL_COMMAND_SET_FAN_AUTOMATION = 					21
    PROTOCOL_COMMAND_GET_FAN_AUTOMATION = 					22
    PROTOCOL_COMMAND_GET_FAN_HEALTH =	                    23
    PROTOCOL_COMMAND_SET_BATTERY_MAX_CHARGE_LEVEL = 		24
    PROTOCOL_COMMAND_GET_BATTERY_MAX_CHARGE_LEVEL = 		25
    PROTOCOL_COMMAND_SET_SAFE_SHUTDOWN_BATTERY_LEVEL = 		26
    PROTOCOL_COMMAND_GET_SAFE_SHUTDOWN_BATTERY_LEVEL = 		27
    PROTOCOL_COMMAND_SET_SAFE_SHUTDOWN_STATUS = 			28
    PROTOCOL_COMMAND_GET_SAFE_SHUTDOWN_STATUS = 			29
    PROTOCOL_COMMAND_GET_WORKING_MODE = 					30
    PROTOCOL_COMMAND_GET_BUTTON1_STATUS = 					31
    PROTOCOL_COMMAND_GET_BUTTON2_STATUS = 					32
    PROTOCOL_COMMAND_SET_RTC_TIME = 						33
    PROTOCOL_COMMAND_GET_RTC_TIME =		 					34
    PROTOCOL_COMMAND_HARD_POWER_OFF =		 				35
    PROTOCOL_COMMAND_SOFT_POWER_OFF =		 				36
    PROTOCOL_COMMAND_HARD_REBOOT =			 				37
    PROTOCOL_COMMAND_SOFT_REBOOT =		 					38
    PROTOCOL_COMAMND_WATCHDOG_ALARM =                       39
    PROTOCOL_COMMAND_GET_BATTERY_DESIGN_CAPACITY = 			40
    PROTOCOL_COMMAND_SET_BATTERY_DESIGN_CAPACITY =			41
    # .
    # .
    # .
    PROTOCOL_COMMAND_CREATE_SCHEDULED_EVENT = 				100
    PROTOCOL_COMMAND_REMOVE_SCHEDULED_EVENT = 				101
    PROTOCOL_COMMAND_REMOVE_ALL_SCHEDULED_EVENTS =          102
    # .
    # .
    # .
    PROTOCOL_COMMAND_GET_FIRMWARE_VER =	 					200

    # Initializer function
    def __init__(self):
        #print("Command Class initialized!")
        pass


    def __del__(self):
        #print("Command Class Destructed")
        pass


    #############################################################
	### I2C Protocol Functions ##################################
	#############################################################
	
	# Function for sending command
    def sendCommand(self):
        global bufferSend
        #print("Sent Command:")
        #print('[{}]'.format(', '.join(hex(x) for x in bufferSend)))
        try:
            bus.write_i2c_block_data(DEVICE_ADDRESS, 0x01, bufferSend)
        except:
            pass
            
       
		

	# Function for checking command according to protocol
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

        if(bufferRecieveIndex == (PROTOCOL_FRAME_SIZE + datalen)):
            
            crcRecieved = (bufferRecieve[PROTOCOL_FRAME_SIZE + datalen -2] << 8) | bufferRecieve[PROTOCOL_FRAME_SIZE + datalen - 1]
            #print("CRC Received: " + str(crcRecieved))
            
            crcCalculated = self.calculateCRC16(bufferRecieve[0:PROTOCOL_HEADER_SIZE+datalen], 1)
            #print("CRC Calculated: " + str(crcCalculated))

            if(crcCalculated == crcRecieved):
                #print("CRC Check OK")
                #print('[{}]'.format(', '.join(hex(x) for x in bufferRecieve)))
                bufferRecieveIndex = 0
                return bufferRecieve[0:PROTOCOL_FRAME_SIZE + datalen]
            else:
                print("CRC Check FAILED!")
                bufferRecieveIndex = 0
                return 0
            


    # Function for recieving command
    def recieveCommand(self, lenOfResponse):
        global bufferRecieve

        for i in range(lenOfResponse):

            try:
                c = bus.read_byte(DEVICE_ADDRESS)
            except:
                print("error in " + str(i))
        
            #print("Recieved byte: " + str(hex(c)))
            msg = self.checkCommand(c)

        if(msg != None and msg != -1):
            bufferRecieve.clear()
            return msg


    # Function for creating command according to protocol
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


    # Function for creating set command according to protocol
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

        if(isinstance(value, int)):
            byteArray = value.to_bytes(lenByte,"big")
        elif(isinstance(value, bytearray)):
            byteArray = value
        else:
            print("Wrong parameter for CreateSetComamnd!")

        for i in range(lenByte):
            bufferSend.append(int(byteArray[i]))

        #print(bufferSend)

        (crcHigh, crcLow) = self.calculateCRC16(bufferSend[0:PROTOCOL_HEADER_SIZE+lenByte])
        bufferSend.append(crcHigh)
        bufferSend.append(crcLow)
        #print(bufferSend)


    # Function for calculating CRC16
    def calculateCRC16(self, command, returnType = 0):
        calCRC = crc16.crc16xmodem(bytes(command))
        crcHigh = (calCRC >> 8) & 0xFF
        crcLow = calCRC & 0xFF
        #print("CRC16: " + str(calCRC) + "\t" + "CRC16 High: " + str(crcHigh) + "\t" + "CRC16 Low: " + str(crcLow))
        
        if(returnType == 0):
            return (crcHigh, crcLow)
        else:
            return calCRC