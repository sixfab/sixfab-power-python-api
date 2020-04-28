#!/usr/bin/python3

from .exceptions import CRCCheckFailed

import smbus2
import time
import struct
import crc16

bus = smbus2.SMBus(1)

#############################################################
### Communication Protocol ##################################
#############################################################
buffer_send = list()
buffer_receive = list()
buffer_recieve_index = 0


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

FIRMWARE_PACKET_LEN =               20

COMMAND_TYPE_REQUEST = 				0x01
COMMAND_TYPE_RESPONSE = 			0x02

DEVICE_ADDRESS =                    0x41        #7 bit address (will be left shifted to add the read write bit)

class Command:

    # API ERRORS
    CRC_CHECK_FAILED = -2
    BYTE_READ_FAILED = -3
    BYTE_SEND_FAILED = -4

    # API COMMANDS
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
    PROTOCOL_COMMAND_HARD_POWER_ON =			 			42
    PROTOCOL_COMMAND_SOFT_POWER_ON =	 					43
    PROTOCOL_COMMAND_IS_ANY_SOFT_ACTION_EXIST =             44
    # .
    # .
    # .
    PROTOCOL_COMMAND_CREATE_SCHEDULED_EVENT = 				100
    PROTOCOL_COMMAND_REMOVE_SCHEDULED_EVENT = 				101
    PROTOCOL_COMMAND_REMOVE_ALL_SCHEDULED_EVENTS =          102
    PROTOCOL_COMMAND_GET_SCHEDULED_EVENT_IDS =              103
    # .
    # .
    # .
    PROTOCOL_COMMAND_GET_FIRMWARE_VER =	 					200
    PROTOCOL_COMMAND_FIRMWARE_UPDATE =						201
    PROTOCOL_COMMAND_WRITE_FIRMWARE_TO_FLASH =				202
    PROTOCOL_COMMAND_RESET_MCU =							203
    PROTOCOL_COMMAND_CLEAR_PROGRAM_STORAGE =                204
    PROTOCOL_COMMAND_CLEAR_PROGRAM_AREA =                   205
    PROTOCOL_COMMAND_RESET_MCU_FOR_BOOT_UPDATE =            206

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
        global buffer_send
        #print("Sent Command:")
        #print('[{}]'.format(', '.join(hex(x) for x in buffer_send)))
        try:
            bus.write_i2c_block_data(DEVICE_ADDRESS, 0x01, buffer_send)
        except:
            return self.BYTE_SEND_FAILED
            
       
		

	# Function for checking command according to protocol
    def checkCommand(self, recievedByte):
        global buffer_receive
        global buffer_recieve_index
        datalen = 0

        if(buffer_recieve_index == 0 and recievedByte != START_BYTE_RECIEVED):
            return -1
            
        buffer_receive.append(recievedByte)
        buffer_recieve_index += 1
        
        if(buffer_recieve_index < PROTOCOL_HEADER_SIZE):
            return -1
        
        datalen = (buffer_receive[3] << 8) | buffer_receive[4]

        if(buffer_recieve_index == (PROTOCOL_FRAME_SIZE + datalen)):
            
            crcRecieved = (buffer_receive[PROTOCOL_FRAME_SIZE + datalen -2] << 8) | buffer_receive[PROTOCOL_FRAME_SIZE + datalen - 1]
            #print("CRC Received: " + str(crcRecieved))
            
            crcCalculated = self.calculateCRC16(buffer_receive[0:PROTOCOL_HEADER_SIZE+datalen], 1)
            #print("CRC Calculated: " + str(crcCalculated))

            if(crcCalculated == crcRecieved):
                #print("CRC Check OK")
                #print('[{}]'.format(', '.join(hex(x) for x in buffer_receive)))
                buffer_recieve_index = 0
                return buffer_receive[0:PROTOCOL_FRAME_SIZE + datalen]
            else:
                print("CRC Check FAILED!")
                buffer_recieve_index = 0
                raise CRCCheckFailed("CRC check failed!")
            


    # Function for recieving command
    def recieveCommand(self, lenOfResponse):
        global buffer_receive

        for i in range(lenOfResponse):

            try:
                c = bus.read_byte(DEVICE_ADDRESS)
            except:
                print("error in " + str(i))
                return self.BYTE_READ_FAILED
        
            #print("Recieved byte: " + str(hex(c)))
            msg = self.checkCommand(c)

        if(msg != None and msg != -1 and msg != self.CRC_CHECK_FAILED):
            buffer_receive.clear()
            return msg
        elif(msg == self.CRC_CHECK_FAILED):
            raise CRCCheckFailed("CRC check failed!")
        else:
            return None


    # Function for creating command according to protocol
    def createCommand(self, command, command_type = COMMAND_TYPE_REQUEST):
        global buffer_send
        buffer_send.clear()
        buffer_send.append(START_BYTE_SENT)
        buffer_send.append(command)
        buffer_send.append(command_type)
        buffer_send.append(0x00)
        buffer_send.append(0x00)
        (crcHigh, crcLow) = self.calculateCRC16(buffer_send[0:PROTOCOL_HEADER_SIZE])
        buffer_send.append(crcHigh)
        buffer_send.append(crcLow)


    # Function for creating set command according to protocol
    def createSetCommand(self, command, value, lenByte, command_type = COMMAND_TYPE_REQUEST):
        global buffer_send
        buffer_send.clear()
        buffer_send.append(START_BYTE_SENT)
        buffer_send.append(command)
        buffer_send.append(command_type)

        lenLow = lenByte & 0xFF
        lenHigh = (lenByte >> 8) & 0xFF

        buffer_send.append(lenHigh)
        buffer_send.append(lenLow)

        if(isinstance(value, int)):
            byteArray = value.to_bytes(lenByte,"big")
        elif(isinstance(value, bytearray)):
            byteArray = value
        else:
            print("Wrong parameter for CreateSetComamnd!")

        for i in range(lenByte):
            buffer_send.append(int(byteArray[i]))

        #print(buffer_send)

        (crcHigh, crcLow) = self.calculateCRC16(buffer_send[0:PROTOCOL_HEADER_SIZE+lenByte])
        buffer_send.append(crcHigh)
        buffer_send.append(crcLow)
        #print(buffer_send)


    def createFirmwareUpdateCommand(self, packet_count, packet_id, packet, packet_len=FIRMWARE_PACKET_LEN):

        global buffer_send
        buffer_send.clear()
        buffer_send.append(START_BYTE_SENT)
        buffer_send.append(self.PROTOCOL_COMMAND_FIRMWARE_UPDATE)
        buffer_send.append(COMMAND_TYPE_REQUEST)

        datalen = packet_len + 4    # packet_len + packet_id_len + packet_count_len 
        lenLow = datalen & 0xFF
        lenHigh = (datalen >> 8) & 0xFF

        buffer_send.append(lenHigh)
        buffer_send.append(lenLow)

        packetCountHigh = (packet_count >> 8) & 0xFF
        packetCountLow = packet_count & 0xFF

        buffer_send.append(packetCountHigh)
        buffer_send.append(packetCountLow)

        packetIdHigh = (packet_id >> 8) & 0xFF
        packetIdLow = packet_id & 0xFF

        buffer_send.append(packetIdHigh)
        buffer_send.append(packetIdLow)

        for i in range(packet_len):
            try:
                buffer_send.append(packet[i])
            except:
                pass
            
        #print(buffer_send)
        (crcHigh, crcLow) = self.calculateCRC16(buffer_send[0:PROTOCOL_HEADER_SIZE+lenLow])
        buffer_send.append(crcHigh)
        buffer_send.append(crcLow)
        #print(buffer_send)

    def createClearCommand(self):
        global buffer_send
        buffer_send.clear()
        
        for i in range(32):
            buffer_send.append(0xFF)


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