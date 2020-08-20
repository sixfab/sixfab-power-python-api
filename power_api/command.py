#!/usr/bin/python3

from power_api.exceptions import crc_check_failed

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
buffer_receive_index = 0


START_BYTE_RECIEVED = 0xDC  # Start Byte Recieved
START_BYTE_SENT = 0xCD  # Start Byte Sent
PROTOCOL_HEADER_SIZE = 5
PROTOCOL_FRAME_SIZE = 7
COMMAND_SIZE_FOR_FLOAT = 11
COMMAND_SIZE_FOR_DOUBLE = 13
COMMAND_SIZE_FOR_INT16 = 9
COMMAND_SIZE_FOR_INT32 = 11
COMMAND_SIZE_FOR_UINT8 = 8
COMMAND_SIZE_FOR_INT64 = 15

FIRMWARE_PACKET_LEN = 20

COMMAND_TYPE_REQUEST = 0x01
COMMAND_TYPE_RESPONSE = 0x02

DEVICE_ADDRESS = 0x41  # 7 bit address (will be left shifted to add the read write bit)


class Command:
    """ 
    Command class for provide i2c communication requirements 
    of Sixfab Power API.
    
    Methods
    -------
    send_command : Function for sending command
    check_command : Function for checking command according to protocol
    receive_command : Function for receiving command
    create_command : Function for creating command according to protocol
    create_set_command : Function for creating set command according to protocol
    createFirmwareUpdateCommand : Function for creating firmware command according to protocol
    calculate_crc16 : Function for calculating CRC16
    """

    # API ERRORS
    CRC_CHECK_FAILED = -2
    BYTE_READ_FAILED = -3
    BYTE_SEND_FAILED = -4

    # API COMMANDS
    PROTOCOL_COMMAND_GET_INPUT_TEMP = 1
    PROTOCOL_COMMAND_GET_INPUT_VOLTAGE = 2
    PROTOCOL_COMMAND_GET_INPUT_CURRENT = 3
    PROTOCOL_COMMAND_GET_INPUT_POWER = 4
    PROTOCOL_COMMAND_GET_SYSTEM_TEMP = 5
    PROTOCOL_COMMAND_GET_SYSTEM_VOLTAGE = 6
    PROTOCOL_COMMAND_GET_SYSTEM_CURRENT = 7
    PROTOCOL_COMMAND_GET_SYSTEM_POWER = 8
    PROTOCOL_COMMAND_GET_BATTERY_TEMP = 9
    PROTOCOL_COMMAND_GET_BATTERY_VOLTAGE = 10
    PROTOCOL_COMMAND_GET_BATTERY_CURRENT = 11
    PROTOCOL_COMMAND_GET_BATTERY_POWER = 12
    PROTOCOL_COMMAND_GET_BATTERY_LEVEL = 13
    PROTOCOL_COMMAND_GET_BATTERY_HEALTH = 14
    PROTOCOL_COMMAND_GET_FAN_SPEED = 15
    PROTOCOL_COMMAND_GET_WATCHDOG_STATUS = 16
    PROTOCOL_COMMAND_SET_WATCHDOG_STATUS = 17
    PROTOCOL_COMMAND_SET_RGB_ANIMATION = 18
    PROTOCOL_COMMAND_GET_RGB_ANIMATION = 19
    PROTOCOL_COMMAND_SET_FAN_SPEED = 20
    PROTOCOL_COMMAND_SET_FAN_AUTOMATION = 21
    PROTOCOL_COMMAND_GET_FAN_AUTOMATION = 22
    PROTOCOL_COMMAND_GET_FAN_HEALTH = 23
    PROTOCOL_COMMAND_SET_BATTERY_MAX_CHARGE_LEVEL = 24
    PROTOCOL_COMMAND_GET_BATTERY_MAX_CHARGE_LEVEL = 25
    PROTOCOL_COMMAND_SET_SAFE_SHUTDOWN_BATTERY_LEVEL = 26
    PROTOCOL_COMMAND_GET_SAFE_SHUTDOWN_BATTERY_LEVEL = 27
    PROTOCOL_COMMAND_SET_SAFE_SHUTDOWN_STATUS = 28
    PROTOCOL_COMMAND_GET_SAFE_SHUTDOWN_STATUS = 29
    PROTOCOL_COMMAND_GET_WORKING_MODE = 30
    PROTOCOL_COMMAND_GET_BUTTON1_STATUS = 31
    PROTOCOL_COMMAND_GET_BUTTON2_STATUS = 32
    PROTOCOL_COMMAND_SET_RTC_TIME = 33
    PROTOCOL_COMMAND_GET_RTC_TIME = 34
    PROTOCOL_COMMAND_HARD_POWER_OFF = 35
    PROTOCOL_COMMAND_SOFT_POWER_OFF = 36
    PROTOCOL_COMMAND_HARD_REBOOT = 37
    PROTOCOL_COMMAND_SOFT_REBOOT = 38
    PROTOCOL_COMAMND_WATCHDOG_ALARM = 39
    PROTOCOL_COMMAND_GET_BATTERY_DESIGN_CAPACITY = 40
    PROTOCOL_COMMAND_SET_BATTERY_DESIGN_CAPACITY = 41
    PROTOCOL_COMMAND_HARD_POWER_ON = 42
    PROTOCOL_COMMAND_SOFT_POWER_ON = 43
    PROTOCOL_COMMAND_IS_ANY_SOFT_ACTION_EXIST = 44
    PROTOCOL_COMMAND_GET_LOW_POWER_MODE = 45
    PROTOCOL_COMMAND_GET_EASY_DEPLOYMENT_MODE = 46
    PROTOCOL_COMMAND_SET_LOW_POWER_MODE = 47
    PROTOCOL_COMMAND_SET_EASY_DEPLOYMENT_MODE = 48
    PROTOCOL_COMMAND_SET_FAN_MODE = 49
    PROTOCOL_COMMAND_GET_FAN_MODE = 50
    # .
    # .
    # .
    PROTOCOL_COMMAND_CREATE_SCHEDULED_EVENT = 100
    PROTOCOL_COMMAND_REMOVE_SCHEDULED_EVENT = 101
    PROTOCOL_COMMAND_REMOVE_ALL_SCHEDULED_EVENTS = 102
    PROTOCOL_COMMAND_GET_SCHEDULED_EVENT_IDS = 103
    # .
    # .
    # .
    PROTOCOL_COMMAND_GET_FIRMWARE_VER = 200
    PROTOCOL_COMMAND_FIRMWARE_UPDATE = 201
    PROTOCOL_COMMAND_WRITE_FIRMWARE_TO_FLASH = 202
    PROTOCOL_COMMAND_RESET_MCU = 203
    PROTOCOL_COMMAND_CLEAR_PROGRAM_STORAGE = 204
    PROTOCOL_COMMAND_CLEAR_PROGRAM_AREA = 205
    PROTOCOL_COMMAND_RESET_MCU_FOR_BOOT_UPDATE = 206

    # Initializer function
    def __init__(self):
        # print("Command Class initialized!")
        pass

    def __del__(self):
        # print("Command Class Destructed")
        pass

    #############################################################
    ### I2C Protocol Functions ##################################
    #############################################################

    # Function for sending command
    def send_command(self):
        global buffer_send
        # print("Sent Command:")
        # print('[{}]'.format(', '.join(hex(x) for x in buffer_send)))
        try:
            bus.write_i2c_block_data(DEVICE_ADDRESS, 0x01, buffer_send)
        except:
            return self.BYTE_SEND_FAILED

    # Function for checking command according to protocol
    def check_command(self, received_byte):
        global buffer_receive
        global buffer_receive_index
        datalen = 0

        if buffer_receive_index == 0 and received_byte != START_BYTE_RECIEVED:
            return -1

        buffer_receive.append(received_byte)
        buffer_receive_index += 1

        if buffer_receive_index < PROTOCOL_HEADER_SIZE:
            return -1

        datalen = (buffer_receive[3] << 8) | buffer_receive[4]

        if datalen > 32:
            # print("="*50)
            # print('[{}]'.format(', '.join(hex(x) for x in buffer_receive)))
            buffer_receive_index = 0
            buffer_receive.clear()

        if buffer_receive_index == (PROTOCOL_FRAME_SIZE + datalen):

            crc_received = (
                buffer_receive[PROTOCOL_FRAME_SIZE + datalen - 2] << 8
            ) | buffer_receive[PROTOCOL_FRAME_SIZE + datalen - 1]
            # print("CRC Received: " + str(crc_received))

            crc_calculated = self.calculate_crc16(
                buffer_receive[0 : PROTOCOL_HEADER_SIZE + datalen], 1
            )
            # print("CRC Calculated: " + str(crc_calculated))

            if crc_calculated == crc_received:
                # print("CRC Check OK")
                # print('[{}]'.format(', '.join(hex(x) for x in buffer_receive)))
                buffer_receive_index = 0
                return buffer_receive[0 : PROTOCOL_FRAME_SIZE + datalen]
            else:
                print("CRC Check FAILED!")
                buffer_receive_index = 0
                raise crc_check_failed("CRC check failed!")

    # Function for receiving command
    def receive_command(self, len_of_response):
        global buffer_receive

        for i in range(len_of_response):

            try:
                c = bus.read_byte(DEVICE_ADDRESS)
            except:
                print("error in " + str(i))
                return self.BYTE_READ_FAILED

            # print("Recieved byte: " + str(hex(c)))
            msg = self.check_command(c)

        if msg != None and msg != -1 and msg != self.CRC_CHECK_FAILED:
            buffer_receive.clear()
            return msg
        elif msg == self.CRC_CHECK_FAILED:
            raise crc_check_failed("CRC check failed!")
        else:
            return None

    # Function for creating command according to protocol
    def create_command(self, command, command_type=COMMAND_TYPE_REQUEST):
        global buffer_send
        buffer_send.clear()
        buffer_send.append(START_BYTE_SENT)
        buffer_send.append(command)
        buffer_send.append(command_type)
        buffer_send.append(0x00)
        buffer_send.append(0x00)
        (crc_high, crc_low) = self.calculate_crc16(buffer_send[0:PROTOCOL_HEADER_SIZE])
        buffer_send.append(crc_high)
        buffer_send.append(crc_low)

    # Function for creating set command according to protocol
    def create_set_command(
        self, command, value, len_byte, command_type=COMMAND_TYPE_REQUEST
    ):
        global buffer_send
        buffer_send.clear()
        buffer_send.append(START_BYTE_SENT)
        buffer_send.append(command)
        buffer_send.append(command_type)

        len_low = len_byte & 0xFF
        len_high = (len_byte >> 8) & 0xFF

        buffer_send.append(len_high)
        buffer_send.append(len_low)

        if isinstance(value, int):
            byte_array = value.to_bytes(len_byte, "big")
        elif isinstance(value, bytearray):
            byte_array = value
        else:
            print("Wrong parameter for CreateSetComamnd!")

        for i in range(len_byte):
            buffer_send.append(int(byte_array[i]))

        # print(buffer_send)

        (crc_high, crc_low) = self.calculate_crc16(
            buffer_send[0 : PROTOCOL_HEADER_SIZE + len_byte]
        )
        buffer_send.append(crc_high)
        buffer_send.append(crc_low)
        # print(buffer_send)

    def create_firmware_update_command(
        self, packet_count, packet_id, packet, packet_len=FIRMWARE_PACKET_LEN
    ):

        global buffer_send
        buffer_send.clear()
        buffer_send.append(START_BYTE_SENT)
        buffer_send.append(self.PROTOCOL_COMMAND_FIRMWARE_UPDATE)
        buffer_send.append(COMMAND_TYPE_REQUEST)

        datalen = packet_len + 4  # packet_len + packet_id_len + packet_count_len
        len_low = datalen & 0xFF
        len_high = (datalen >> 8) & 0xFF

        buffer_send.append(len_high)
        buffer_send.append(len_low)

        packet_count_high = (packet_count >> 8) & 0xFF
        packet_count_low = packet_count & 0xFF

        buffer_send.append(packet_count_high)
        buffer_send.append(packet_count_low)

        packet_id_high = (packet_id >> 8) & 0xFF
        packet_id_low = packet_id & 0xFF

        buffer_send.append(packet_id_high)
        buffer_send.append(packet_id_low)

        for i in range(packet_len):
            try:
                buffer_send.append(packet[i])
            except:
                pass

        # print(buffer_send)
        (crc_high, crc_low) = self.calculate_crc16(
            buffer_send[0 : PROTOCOL_HEADER_SIZE + len_low]
        )
        buffer_send.append(crc_high)
        buffer_send.append(crc_low)
        # print(buffer_send)

    # Function for calculating CRC16
    def calculate_crc16(self, command, return_type=0):
        cal_crc = crc16.crc16xmodem(bytes(command))
        crc_high = (cal_crc >> 8) & 0xFF
        crc_low = cal_crc & 0xFF
        # print("CRC16: " + str(cal_crc) + "\t" + "CRC16 High: " + str(crc_high) + "\t" + "CRC16 Low: " + str(crc_low))

        if return_type == 0:
            return (crc_high, crc_low)
        else:
            return cal_crc
