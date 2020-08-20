#!/usr/bin/python3

import time
import datetime
from power_api.command import Command
from power_api.definitions import Definition
from power_api.event import Event
import os

command = Command()

#############################################################
### Communication Protocol ##################################
#############################################################
buffer_send = list()
buffer_receive = list()
buffer_recieve_index = 0

RESPONSE_DELAY = 10

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

COMMAND_TYPE_REQUEST = 0x01
COMMAND_TYPE_RESPONSE = 0x02

DEVICE_ADDRESS = 0x41  # 7 bit address (will be left shifted to add the read write bit)


###########################################
### Private Methods #######################
###########################################


def debug_print(message):
    """Function for printing debug message."""
    print(message)


def millis():
    """Function for getting time as miliseconds."""
    return int(time.time())


def delay_ms(ms):
    """Function for delay as miliseconds."""
    time.sleep(float(ms / 1000.0))


#############################################################
### SIXFAB POWER CLASS ######################################
#############################################################
class SixfabPower:
    """ 
    Sixfab Power Class.
    
    """

    board = "Sixfab Raspberry Pi UPS HAT"

    # Initializer function
    def __init__(self):
        # debug_print(self.board + " Class initialized!")
        pass

    def __del__(self):
        # print("Class Destructed")
        pass

    #############################################################
    ### API Call Methods ########################################
    #############################################################

    def get_input_temp(self, timeout=RESPONSE_DELAY):
        """Function for getting input temperature
        
        Parameters
        -----------		
        timeout : int (optional)
        timeout while receiving the response (default is RESPONSE_DELAY)

        Returns
        ------- 
        temperature : float 
        PCB temperature of Sixfab Power Management and UPS HAT [Celcius]  
        """

        command.create_command(command.PROTOCOL_COMMAND_GET_INPUT_TEMP)
        command.send_command()
        delay_ms(timeout)
        raw = command.receive_command(COMMAND_SIZE_FOR_INT32)

        temp = int.from_bytes(
            raw[PROTOCOL_HEADER_SIZE : COMMAND_SIZE_FOR_INT32 - 2], "big"
        )
        return temp / 100

    def get_input_voltage(self, timeout=RESPONSE_DELAY):
        """
        Function for getting input voltage
        
        Parameters
        -----------	
        timeout : int (optional)
            timeout while receiving the response (default is RESPONSE_DELAY)

        Returns
        ------- 
        voltage : float 
            input voltage [Volt] 
        """

        command.create_command(command.PROTOCOL_COMMAND_GET_INPUT_VOLTAGE)
        command.send_command()
        delay_ms(timeout)
        raw = command.receive_command(COMMAND_SIZE_FOR_INT32)

        voltage = int.from_bytes(
            raw[PROTOCOL_HEADER_SIZE : COMMAND_SIZE_FOR_INT32 - 2], "big"
        )
        return voltage / 1000

    def get_input_current(self, timeout=RESPONSE_DELAY):
        """
        Function for getting input current
        
        Parameters
        -----------			
        timeout : int (optional)
            timeout while receiving the response (default is RESPONSE_DELAY)

        Returns
        ------- 
        current : float 
            input current [Ampere] 
        """

        command.create_command(command.PROTOCOL_COMMAND_GET_INPUT_CURRENT)
        command.send_command()
        delay_ms(timeout)
        raw = command.receive_command(COMMAND_SIZE_FOR_INT32)

        current = int.from_bytes(
            raw[PROTOCOL_HEADER_SIZE : COMMAND_SIZE_FOR_INT32 - 2], "big"
        )
        return current / 1000

    def get_input_power(self, timeout=50):
        """
        Function for getting input power
        
        Parameters
        -----------
        timeout : int (optional)
            timeout while receiving the response (default is RESPONSE_DELAY)

        Returns
        ------- 
        power : float
            input power [Watt] 
        """

        command.create_command(command.PROTOCOL_COMMAND_GET_INPUT_POWER)
        command.send_command()
        delay_ms(timeout)
        raw = command.receive_command(COMMAND_SIZE_FOR_INT32)

        power = int.from_bytes(
            raw[PROTOCOL_HEADER_SIZE : COMMAND_SIZE_FOR_INT32 - 2], "big"
        )
        return power / 1000

    def get_system_temp(self):
        """
        Function for getting raspberry pi core temperature
        
        Parameters
        -----------	
        None

        Returns
        ------- 
        temperature : float
            raspberry pi core temperature [Celcius] 
        """
        temp = os.popen("vcgencmd measure_temp").readline()
        temp = temp.replace("temp=", "")
        return float(temp[:-3])

    def send_system_temp(self, timeout=10):
        """
        Function for sending raspberry pi core temperature to mcu
        
        Parameters
        -----------	
        timeout : int (optional)
            timeout while receiving the response (default is RESPONSE_DELAY)

        Returns
        ------- 
        result : int
            "1" for SUCCESS, "2" for FAIL
        """

        temp = self.get_system_temp()
        tempInt = int(temp * 100)

        command.create_set_command(command.PROTOCOL_COMMAND_GET_SYSTEM_TEMP, tempInt, 4)
        command.send_command()
        delay_ms(timeout)
        raw = command.receive_command(COMMAND_SIZE_FOR_UINT8)

        result = raw[PROTOCOL_HEADER_SIZE]
        return result

    def get_system_voltage(self, timeout=RESPONSE_DELAY):
        """
        Function for getting system voltage
        
        Parameters
        -----------
        timeout : int (optional)
            timeout while receiving the response (default is RESPONSE_DELAY)

        Returns
        ------- 
        voltage : float
            voltage source that supplies raspberry pi and other peripherals [Volt]
        """

        command.create_command(command.PROTOCOL_COMMAND_GET_SYSTEM_VOLTAGE)
        command.send_command()
        delay_ms(timeout)
        raw = command.receive_command(COMMAND_SIZE_FOR_INT32)

        voltage = int.from_bytes(
            raw[PROTOCOL_HEADER_SIZE : COMMAND_SIZE_FOR_INT32 - 2], "big"
        )
        return voltage / 1000

    def get_system_current(self, timeout=50):
        """
        Function for getting system current
        
        Parameters
        -----------	
        timeout : int (optional)
            timeout while receiving the response (default is RESPONSE_DELAY)

        Returns
        ------- 
        current : float
            current that supplies raspberry pi and other peripherals [Ampere]
        """
        command.create_command(command.PROTOCOL_COMMAND_GET_SYSTEM_CURRENT)
        command.send_command()
        delay_ms(timeout)
        raw = command.receive_command(COMMAND_SIZE_FOR_INT32)

        current = int.from_bytes(
            raw[PROTOCOL_HEADER_SIZE : COMMAND_SIZE_FOR_INT32 - 2], "big"
        )
        return current / 1000

    def get_system_power(self, timeout=50):
        """
        Function for getting system power
        
        Parameters
        -----------	
        timeout : int (optional)
            timeout while receiving the response (default is RESPONSE_DELAY)

        Returns
        ------- 
        power : float
            power that supplies raspberry pi and other peripherals [Ampere]
        """
        command.create_command(command.PROTOCOL_COMMAND_GET_SYSTEM_POWER)
        command.send_command()
        delay_ms(timeout)
        raw = command.receive_command(COMMAND_SIZE_FOR_INT32)

        power = int.from_bytes(
            raw[PROTOCOL_HEADER_SIZE : COMMAND_SIZE_FOR_INT32 - 2], "big"
        )
        return power / 1000

    def get_battery_temp(self, timeout=RESPONSE_DELAY):
        """
        Function for getting battery temperature
        
        Parameters
        -----------
        timeout : int (optional)
            timeout while receiving the response (default is RESPONSE_DELAY)

        Returns
        ------- 
        temperature : float
            battery temperature [Celcius]
        """

        command.create_command(command.PROTOCOL_COMMAND_GET_BATTERY_TEMP)
        command.send_command()
        delay_ms(timeout)
        raw = command.receive_command(COMMAND_SIZE_FOR_INT32)

        temp = int.from_bytes(
            raw[PROTOCOL_HEADER_SIZE : COMMAND_SIZE_FOR_INT32 - 2], "big"
        )
        return temp / 100

    def get_battery_voltage(self, timeout=RESPONSE_DELAY):
        """
        Function for getting battery voltage
        
        Parameters
        -----------
        timeout : int (optional)
            timeout while receiving the response (default is RESPONSE_DELAY)

        Returns
        ------- 
        voltage : float 
            battery voltage [Volt]
        """
        command.create_command(command.PROTOCOL_COMMAND_GET_BATTERY_VOLTAGE)
        command.send_command()
        delay_ms(timeout)
        raw = command.receive_command(COMMAND_SIZE_FOR_INT32)

        voltage = int.from_bytes(
            raw[PROTOCOL_HEADER_SIZE : COMMAND_SIZE_FOR_INT32 - 2], "big"
        )
        return voltage / 1000

    def get_battery_current(self, timeout=RESPONSE_DELAY):
        """
        Function for getting battery current
        
        Parameters
        -----------
        timeout : int (optional)
            timeout while receiving the response (default is RESPONSE_DELAY)

        Returns
        ------- 
        current : float
            battery current [Ampere]
        """

        command.create_command(command.PROTOCOL_COMMAND_GET_BATTERY_CURRENT)
        command.send_command()
        delay_ms(timeout)
        raw = command.receive_command(COMMAND_SIZE_FOR_INT32)

        current = int.from_bytes(
            raw[PROTOCOL_HEADER_SIZE : COMMAND_SIZE_FOR_INT32 - 2], "big", signed=True
        )
        return current / 1000

    def get_battery_power(self, timeout=RESPONSE_DELAY):
        """
        Function for getting battery power
        
        Parameters
        -----------
        timeout : int (optional)
            timeout while receiving the response (default is RESPONSE_DELAY)

        Returns
        ------- 
        power : float
            battery power [Watt]
        """

        command.create_command(command.PROTOCOL_COMMAND_GET_BATTERY_POWER)
        command.send_command()
        delay_ms(timeout)
        raw = command.receive_command(COMMAND_SIZE_FOR_INT32)

        power = int.from_bytes(
            raw[PROTOCOL_HEADER_SIZE : COMMAND_SIZE_FOR_INT32 - 2], "big", signed=True
        )
        return power / 1000

    def get_battery_level(self, timeout=RESPONSE_DELAY):
        """
        Function for getting battery level
        
        Parameters
        -----------
        timeout : int (optional)
            timeout while receiving the response (default is RESPONSE_DELAY)

        Returns
        ------- 
        level : int
            battery charge of state as percentage [%]
        """

        command.create_command(command.PROTOCOL_COMMAND_GET_BATTERY_LEVEL)
        command.send_command()
        delay_ms(timeout)
        raw = command.receive_command(COMMAND_SIZE_FOR_INT32)

        level = int.from_bytes(
            raw[PROTOCOL_HEADER_SIZE : COMMAND_SIZE_FOR_INT32 - 2], "big"
        )
        return level

    def get_fan_health(self, timeout=RESPONSE_DELAY):
        """
        Function for getting fan health
        
        Parameters
        -----------
        timeout : int (optional)
            timeout while receiving the response (default is RESPONSE_DELAY)

        Returns
        ------- 
        health : int
            "1" for HEALTHY, "2" for BROKEN
        """

        command.create_command(command.PROTOCOL_COMMAND_GET_FAN_HEALTH)
        command.send_command()
        delay_ms(timeout)
        raw = command.receive_command(COMMAND_SIZE_FOR_INT32)

        health = int.from_bytes(
            raw[PROTOCOL_HEADER_SIZE : COMMAND_SIZE_FOR_INT32 - 2], "big"
        )
        return health

    def get_battery_health(self, timeout=RESPONSE_DELAY):
        """
        Function for getting battery health
        
        Parameters
        -----------
        timeout : int (optional)
            timeout while receiving the response (default is RESPONSE_DELAY)

        Returns
        ------- 
        health : int
            battery health as percentage [%] 
        """
        command.create_command(command.PROTOCOL_COMMAND_GET_BATTERY_HEALTH)
        command.send_command()
        delay_ms(timeout)
        raw = command.receive_command(COMMAND_SIZE_FOR_INT32)

        health = int.from_bytes(
            raw[PROTOCOL_HEADER_SIZE : COMMAND_SIZE_FOR_INT32 - 2], "big"
        )
        return health

    def get_fan_speed(self, timeout=RESPONSE_DELAY):
        """
        Function for getting fan speed
        
        Parameters
        -----------
        timeout : int (optional)
            timeout while receiving the response (default is RESPONSE_DELAY)

        Returns
        ------- 
        speed : int
            fan speed [RPM] 
        """

        command.create_command(command.PROTOCOL_COMMAND_GET_FAN_SPEED)
        command.send_command()
        delay_ms(timeout)
        raw = command.receive_command(COMMAND_SIZE_FOR_INT32)

        rpm = int.from_bytes(
            raw[PROTOCOL_HEADER_SIZE : COMMAND_SIZE_FOR_INT32 - 2], "big"
        )
        return rpm


    def get_watchdog_status(self, timeout=RESPONSE_DELAY):
        """
        Function for getting watchdog status
        
        Parameters
        -----------
        timeout : int (optional)
            timeout while receiving the response (default is RESPONSE_DELAY)

        Returns
        ------- 
        status : int
            "1" for WATCHDOG ENABLED, "2" for WATCHDOG DISABLED 
        """

        command.create_command(command.PROTOCOL_COMMAND_GET_WATCHDOG_STATUS)
        command.send_command()
        delay_ms(timeout)
        raw = command.receive_command(COMMAND_SIZE_FOR_UINT8)

        status = raw[PROTOCOL_HEADER_SIZE]
        return status

    def set_watchdog_status(self, status, timeout=RESPONSE_DELAY):
        """
        Function for setting watchdog status
        
        Parameters
        -----------
        status : "1" for WATCHDOG ENABLED, "2" for WATCHDOG DISABLED
        timeout : int (optional)
            timeout while receiving the response (default is RESPONSE_DELAY)

        Returns
        ------- 
        result : int
            "1" for SET OK, "2" for SET FAILED 
        """

        command.create_set_command(
            command.PROTOCOL_COMMAND_SET_WATCHDOG_STATUS, status, 1
        )
        command.send_command()
        delay_ms(timeout)
        raw = command.receive_command(COMMAND_SIZE_FOR_UINT8)

        result = raw[PROTOCOL_HEADER_SIZE]
        return result

    def set_rgb_animation(self, anim_type, color, speed, timeout=RESPONSE_DELAY):
        """
        Function for setting RGB animation
        
        Parameters
        -----------
        anim_type : [DISABLED, HEARTBEAT, TEMP_MAP]
        color : [GREEN, BLUE, RED, YELLOW, CYAN, MAGENTA, WHITE]
        speed : [SLOW, NORMAL, FAST] 
        timeout : int (optional)
            timeout while receiving the response (default is RESPONSE_DELAY)

        Returns
        ------- 
        result : int
            "1" for SET OK, "2" for SET FAILED 
        """

        value = bytearray()
        value.append(int(anim_type))
        value.append(int(color))
        value.append(int(speed))

        command.create_set_command(command.PROTOCOL_COMMAND_SET_RGB_ANIMATION, value, 3)
        command.send_command()
        delay_ms(timeout)
        raw = command.receive_command(COMMAND_SIZE_FOR_UINT8)

        result = raw[PROTOCOL_HEADER_SIZE]
        return result

    def get_rgb_animation(self, timeout=RESPONSE_DELAY):
        """
        Function for getting RGB animation
        
        Parameters
        -----------
        timeout : int (optional)
            timeout while receiving the response (default is RESPONSE_DELAY)

        Returns
        ------- 
        animation : byteArray(3)
            [anim_type, color, speed]

        Notes
        -----
        anim_type : Definition Object Property
            --> Definition.RGB_DISABLED
            --> Definition.RGB_HEARTBEAT
            --> Definition.RGB_TEMP_MAP

        color : Definition Object Property
            --> Definition.RED
            --> Definition.GREEN
            --> Definition.BLUE
            --> Definition.YELLOW
            --> Definition.CYAN
            --> Definition.MAGENTA
            --> Definition.WHITE
            --> Definition.BLACK
        
        speed : Definition Object Property
            --> Definition.SLOW
            --> Definition.NORMAL
            --> Definition.FAST
        """

        command.create_command(command.PROTOCOL_COMMAND_GET_RGB_ANIMATION)
        command.send_command()
        delay_ms(timeout)
        raw = command.receive_command(10)

        animation = bytearray()
        for i in range(3):
            animation.append(raw[PROTOCOL_HEADER_SIZE + i])

        return animation

    def set_fan_automation(
        self, slow_threshold, fast_threshold=100, timeout=RESPONSE_DELAY
    ):
        """
        Function for setting fan automation
        
        Parameters
        -----------
        slow_threshold : int
            temperature threshold to decide fan working status
        timeout : int (optional)
            timeout while receiving the response (default is RESPONSE_DELAY)

        Returns
        ------- 
        result : int
            "1" for SET OK, "2" for SET FAILED 
        """

        value = bytearray()
        value.append(int(slow_threshold))
        value.append(int(fast_threshold))

        command.create_set_command(
            command.PROTOCOL_COMMAND_SET_FAN_AUTOMATION, value, 2
        )
        command.send_command()
        delay_ms(timeout)
        raw = command.receive_command(COMMAND_SIZE_FOR_UINT8)

        result = raw[PROTOCOL_HEADER_SIZE]
        return result

    def get_fan_automation(self, timeout=RESPONSE_DELAY):
        """
        Function for getting fan automation
        
        Parameters
        -----------
        timeout : int (optional)
            timeout while receiving the response (default is RESPONSE_DELAY)

        Returns
        ------- 
        automation : byteArray(2) 
            [slow_threshold, fast_threshold] [Celcius]
        """

        command.create_command(command.PROTOCOL_COMMAND_GET_FAN_AUTOMATION)
        command.send_command()
        delay_ms(timeout)
        raw = command.receive_command(9)

        fanAutomation = bytearray()
        for i in range(2):
            fanAutomation.append(raw[PROTOCOL_HEADER_SIZE + i])

        return fanAutomation

    def set_battery_max_charge_level(self, level, timeout=RESPONSE_DELAY):
        """
        Function for setting battery max charge level
        
        Parameters
        -----------
        level : int
            battery is charged up to this level in percentage [%]
        timeout : int (optional)
            timeout while receiving the response (default is RESPONSE_DELAY)

        Returns
        ------- 
        result : int
            "1" for SET OK, "2" for SET FAILED
        """

        command.create_set_command(
            command.PROTOCOL_COMMAND_SET_BATTERY_MAX_CHARGE_LEVEL, level, 1
        )
        command.send_command()
        delay_ms(timeout)
        raw = command.receive_command(COMMAND_SIZE_FOR_UINT8)

        level = raw[PROTOCOL_HEADER_SIZE]
        return level

    def get_battery_max_charge_level(self, timeout=RESPONSE_DELAY):
        """
        Function for getting battery max charge level
        
        Parameters
        -----------
        timeout : int (optional)
            timeout while receiving the response (default is RESPONSE_DELAY)

        Returns
        ------- 
        level : int
            battery max charge level in percentage [%]
        """

        command.create_command(command.PROTOCOL_COMMAND_GET_BATTERY_MAX_CHARGE_LEVEL)
        command.send_command()
        delay_ms(timeout)
        raw = command.receive_command(COMMAND_SIZE_FOR_UINT8)

        level = raw[PROTOCOL_HEADER_SIZE]
        return level

    def set_safe_shutdown_battery_level(self, level, timeout=RESPONSE_DELAY):
        """
        Function for setting safe shutdown battery level
        
        Parameters
        -----------
        level : int
            raspberry pi is turned off if battery falls to this level
        timeout : int (optional)
            timeout while receiving the response (default is RESPONSE_DELAY)

        Returns
        ------- 
        result : int
            "1" for SET OK, "2" for SET FAILED
        """

        command.create_set_command(
            command.PROTOCOL_COMMAND_SET_SAFE_SHUTDOWN_BATTERY_LEVEL, level, 1
        )
        command.send_command()
        delay_ms(timeout)
        raw = command.receive_command(COMMAND_SIZE_FOR_UINT8)

        level = raw[PROTOCOL_HEADER_SIZE]
        return level

    def get_safe_shutdown_battery_level(self, timeout=RESPONSE_DELAY):
        """
        Function for setting safe shutdown battery level
        
        Parameters
        -----------
        timeout : int (optional)
            timeout while receiving the response (default is RESPONSE_DELAY)

        Returns
        ------- 
        level : int
            safe shutdown level in percentage [%]
        """

        command.create_command(command.PROTOCOL_COMMAND_GET_SAFE_SHUTDOWN_BATTERY_LEVEL)
        command.send_command()
        delay_ms(timeout)
        raw = command.receive_command(COMMAND_SIZE_FOR_UINT8)

        level = raw[PROTOCOL_HEADER_SIZE]
        return level

    def set_safe_shutdown_status(self, status, timeout=RESPONSE_DELAY):
        """
        Function for setting safe shutdown status
        
        Parameters
        -----------
        status : int
            "1" for ENABLED, "2" for DISABLED
        timeout : int (optional)
            timeout while receiving the response (default is RESPONSE_DELAY)

        Returns
        ------- 
        result : int
            "1" for SET OK, "2" for SET FAILED
        """

        command.create_set_command(
            command.PROTOCOL_COMMAND_SET_SAFE_SHUTDOWN_STATUS, status, 1
        )
        command.send_command()
        delay_ms(timeout)
        raw = command.receive_command(COMMAND_SIZE_FOR_UINT8)

        status = raw[PROTOCOL_HEADER_SIZE]
        return status

    def get_safe_shutdown_status(self, timeout=RESPONSE_DELAY):
        """
        Function for getting safe shutdown status
        
        Parameters
        -----------
        timeout : int (optional)
            timeout while receiving the response (default is RESPONSE_DELAY)

        Returns
        ------- 
        status : int
            "1" for ENABLEDi "2" for DISABLED
        """

        command.create_command(command.PROTOCOL_COMMAND_GET_SAFE_SHUTDOWN_STATUS)
        command.send_command()
        delay_ms(timeout)
        raw = command.receive_command(COMMAND_SIZE_FOR_UINT8)

        status = raw[PROTOCOL_HEADER_SIZE]
        return status

    def get_working_mode(self, timeout=RESPONSE_DELAY):
        """
        Function for getting working mode
        
        Parameters
        -----------
        timeout : int (optional)
            timeout while receiving the response (default is RESPONSE_DELAY)

        Returns
        ------- 
        working_mode : int
            "1" for CHARGING, "2" for FULLY_CHARGED, "3" for BATTERY POWERED
        """

        command.create_command(command.PROTOCOL_COMMAND_GET_WORKING_MODE)
        command.send_command()
        delay_ms(timeout)
        raw = command.receive_command(COMMAND_SIZE_FOR_UINT8)

        mode = raw[PROTOCOL_HEADER_SIZE]
        return mode

    def get_button1_status(self, timeout=RESPONSE_DELAY):
        """
        Function for getting button 1
        
        Parameters
        -----------
        timeout : int (optional)
            timeout while receiving the response (default is RESPONSE_DELAY)

        Returns
        ------- 
        status : int
            "1" for SHORT_PRESS, "2" for LONG_PRESS, "3" for RELEASED
        """

        command.create_command(command.PROTOCOL_COMMAND_GET_BUTTON1_STATUS)
        command.send_command()
        delay_ms(timeout)
        raw = command.receive_command(COMMAND_SIZE_FOR_UINT8)

        status = raw[PROTOCOL_HEADER_SIZE]
        return status

    def get_button2_status(self, timeout=RESPONSE_DELAY):
        """
        Function for getting button 2
        
        Parameters
        -----------
        timeout : int (optional)
            timeout while receiving the response (default is RESPONSE_DELAY)

        Returns
        ------- 
        status : int
            "1" for SHORT_PRESS, "2" for LONG_PRESS, "3" for RELEASED
        """

        command.create_command(command.PROTOCOL_COMMAND_GET_BUTTON2_STATUS)
        command.send_command()
        delay_ms(timeout)
        raw = command.receive_command(COMMAND_SIZE_FOR_UINT8)

        status = raw[PROTOCOL_HEADER_SIZE]
        return status

    def set_rtc_time(self, timestamp, timeout=RESPONSE_DELAY):
        """
        Function for setting time of RTC in MCU
        
        Parameters
        -----------
        time : int
            epoch time
        timeout : int (optional)
            timeout while receiving the response (default is RESPONSE_DELAY)

        Returns
        ------- 
        result : int
            "1" for SET_OK, "2" for SET_FAILED
        """

        command.create_set_command(command.PROTOCOL_COMMAND_SET_RTC_TIME, timestamp, 4)
        command.send_command()
        delay_ms(timeout)
        raw = command.receive_command(COMMAND_SIZE_FOR_UINT8)

        result = raw[PROTOCOL_HEADER_SIZE]
        return result

    def get_rtc_time(self, format=Definition.TIME_FORMAT_EPOCH, timeout=RESPONSE_DELAY):
        """
        Function for getting time of RTC in MCU
        
        Parameters
        -----------
        format : Definition Object Property
            --> Definition.TIME_FORMAT_EPOCH
            --> Definition.TIME_FORMAT_DATE_AND_TIME
            --> Definition.TIME_FORMAT_DATE
            --> Definition.TIME_FORMAT_TIME
        timeout : int (optional)
            timeout while receiving the response (default is RESPONSE_DELAY)

        Returns
        ------- 
        timestamp : int/str
            time in chosen format
        """

        command.create_command(command.PROTOCOL_COMMAND_GET_RTC_TIME)
        command.send_command()
        delay_ms(timeout)
        raw = command.receive_command(COMMAND_SIZE_FOR_INT32)

        timestamp = int.from_bytes(
            raw[PROTOCOL_HEADER_SIZE : COMMAND_SIZE_FOR_INT32 - 2], "big"
        )

        if format == Definition.TIME_FORMAT_EPOCH:
            return timestamp
        elif format == Definition.TIME_FORMAT_DATE_AND_TIME:
            date_and_time = datetime.datetime.utcfromtimestamp(timestamp).strftime(
                "%Y-%m-%d %H:%M:%S"
            )
            return date_and_time
        elif format == Definition.TIME_FORMAT_DATE:
            date = datetime.datetime.utcfromtimestamp(timestamp).strftime("%Y-%m-%d")
            return date
        elif format == Definition.TIME_FORMAT_TIME:
            time = datetime.datetime.utcfromtimestamp(timestamp).strftime("%H:%M:%S")
            return time

    def hard_power_off(self, timeout=RESPONSE_DELAY):
        """
        Function for raspberry pi hard powering off
        
        Parameters
        -----------
        timeout : int (optional)
            timeout while receiving the response (default is RESPONSE_DELAY)

        Returns
        ------- 
        result : int
            "1" for SET_OK, "2" for SET_FAILED
        """

        command.create_command(command.PROTOCOL_COMMAND_HARD_POWER_OFF)
        command.send_command()
        delay_ms(timeout)
        raw = command.receive_command(COMMAND_SIZE_FOR_UINT8)

        result = raw[PROTOCOL_HEADER_SIZE]
        return result

    def soft_power_off(self, timeout=RESPONSE_DELAY):
        """
        Function for checking any soft power off request is exist. If any
        request exist, raspberry pi turns off by using "sudo shutdown" terminal
        command in 5 seconds.
        
        Parameters
        -----------
        timeout : int (optional)
            timeout while receiving the response (default is RESPONSE_DELAY)

        Returns
        ------- 
        result : int
            "1" for EXIST, "2" for NOT_EXIST
        """

        command.create_command(command.PROTOCOL_COMMAND_SOFT_POWER_OFF)
        command.send_command()
        delay_ms(timeout)
        raw = command.receive_command(COMMAND_SIZE_FOR_UINT8)
        result2 = 0
        result = raw[PROTOCOL_HEADER_SIZE]

        if result == Definition.SET_OK:
            command.create_set_command(command.PROTOCOL_COMMAND_SOFT_POWER_OFF, 1, 1)
            command.send_command()
            delay_ms(timeout)
            raw = command.receive_command(COMMAND_SIZE_FOR_UINT8)
            result2 = raw[PROTOCOL_HEADER_SIZE]

            if result2 == Definition.SET_OK:
                print("Raspberry Pi will shutdown in 5 seconds!")
                os.system("sleep 5 && sudo shutdown -h now")
                return result2

        return Definition.SET_FAILED

    def hard_reboot(self, timeout=100):
        """
        Function for hard rebooting
        
        Parameters
        -----------
        timeout : int (optional)
            timeout while receiving the response (default is RESPONSE_DELAY)

        Returns
        ------- 
        result : int
            "1" SET_OK, "2" for SET_FAILED
        """

        command.create_command(command.PROTOCOL_COMMAND_HARD_REBOOT)
        command.send_command()
        delay_ms(timeout)
        raw = command.receive_command(COMMAND_SIZE_FOR_UINT8)

        result = raw[PROTOCOL_HEADER_SIZE]
        return result

    def soft_reboot(self, timeout=RESPONSE_DELAY):
        """
        Function for checking any soft reboot request is exist. If any
        request exist, raspberry pi reboots by using "sudo reboot" terminal
        command in 5 seconds.
        
        Parameters
        -----------
        timeout : int (optional)
            timeout while receiving the response (default is RESPONSE_DELAY)

        Returns
        ------- 
        result : int
            "1" for EXIST, "2" for NOT_EXIST
        """

        command.create_command(command.PROTOCOL_COMMAND_SOFT_REBOOT)
        command.send_command()
        delay_ms(timeout)
        raw = command.receive_command(COMMAND_SIZE_FOR_UINT8)

        result2 = 0
        result = raw[PROTOCOL_HEADER_SIZE]

        if result == Definition.SET_OK:
            command.create_set_command(command.PROTOCOL_COMMAND_SOFT_REBOOT, 1, 1)
            command.send_command()
            delay_ms(timeout)
            raw = command.receive_command(COMMAND_SIZE_FOR_UINT8)
            result2 = raw[PROTOCOL_HEADER_SIZE]

            if result2 == Definition.SET_OK:
                print("Raspberry Pi will shutdown in 5 seconds!")
                os.system("sleep 5 && sudo reboot")
                return result2

        return Definition.SET_FAILED

    def ask_watchdog_alarm(self, timeout=RESPONSE_DELAY):
        """
        Function for asking watchdog alarm is exist
            
        Parameters
        -----------
        timeout : int (optional)
            timeout while receiving the response (default is RESPONSE_DELAY)

        Returns
        ------- 
        result : int
            "1" for EXIST, "2" for NOT_EXIST
        """

        command.create_command(command.PROTOCOL_COMAMND_WATCHDOG_ALARM)
        command.send_command()
        delay_ms(timeout)
        raw = command.receive_command(COMMAND_SIZE_FOR_INT16)

        alarm_status = int.from_bytes(
            raw[PROTOCOL_HEADER_SIZE : COMMAND_SIZE_FOR_INT16 - 2], "big"
        )
        return alarm_status

    def get_battery_design_capacity(self, timeout=RESPONSE_DELAY):
        """
        Function for getting battery design capacity
        
        Parameters
        -----------
        timeout : int (optional)
            timeout while receiving the response (default is RESPONSE_DELAY)

        Returns
        ------- 
        capacity : int
            battery design capacity in [mAh]
        """
        command.create_command(command.PROTOCOL_COMMAND_GET_BATTERY_DESIGN_CAPACITY)
        command.send_command()
        delay_ms(timeout)
        raw = command.receive_command(COMMAND_SIZE_FOR_INT16)

        capacity = int.from_bytes(
            raw[PROTOCOL_HEADER_SIZE : COMMAND_SIZE_FOR_INT16 - 2], "big"
        )
        return capacity

    def set_battery_design_capacity(self, capacity, timeout=RESPONSE_DELAY):
        """
        Function for setting battery design capacity
        
        Parameters
        -----------
        capacity : int
            battery design capacity in [mAh]
        timeout : int (optional)
            timeout while receiving the response (default is RESPONSE_DELAY)

        Returns
        ------- 
        result : int
            "1" for SET_OK, "2" for SET_FAILED 
        """

        command.create_set_command(
            command.PROTOCOL_COMMAND_SET_BATTERY_DESIGN_CAPACITY, capacity, 2
        )
        command.send_command()
        delay_ms(timeout)
        raw = command.receive_command(COMMAND_SIZE_FOR_UINT8)

        status = raw[PROTOCOL_HEADER_SIZE]
        return status

    def create_scheduled_event(
        self,
        event_id,
        schedule_type,
        repeat,
        time_or_interval,
        interval_type,
        repeat_period,
        action,
        timeout=200,
    ):
        """
        Function for creating scheduling event
        
        Parameters
        -----------
        event_id : int 
            id to describe events indivudially

        schedule_type : Definition Object Property
            --> Definition.NO_EVENT
            --> Definition.EVENT_TIME
            --> Definition.EVENT_INTERVAL

        repeat : Definition Object Property
            --> Definition.EVENT_ONE_SHOT
            --> Definition.EVENT_REPEATED

        time_or_interval : int
            daily_epoch_time in seconds or interval (Checkout *Notes for daily_exact_time)

        interval_type : Definition Object Property 
            --> Definition.INTERVAL_TYPE_SEC
            --> Definition.INTERVAL_TYPE_MIN
            --> Definition.INTERVAL_TYPE_HOUR 

        repeat_period : int
            day_factor (Checkout *Notes)

        action : int
            --> "1" for START
            --> "2" for HARD SHUTDOWN
            --> "3" for SOFT SHUTDOWN
            --> "4" for HARD REBOOT
            --> "5" for SOFT REBOOT

         timeout : int (optional)
            timeout while receiving the response (default is RESPONSE_DELAY)

        Notes
        -----
        1) Calculation of daily_exact_time :
        daily exact_time formula: epoch_time_local % (24*60*60)
        
        daily exact time example: 
        --> Friday, March 27, 2020 11:19:00 PM GMT+03:00
        --> epoch_local = 1585340340 (In this case local : GMT+3)
        --> daily exact_time = 1585340340 % 86400 = 73140
        
        2) Calculation of day_factor 								 
        [monday] --> Bit 0
        [tuesday] --> Bit 1
        [wednesday] --> Bit 2
        [thursday] --> Bit 3
        [friday] --> Bit 4
        [saturday] --> Bit 5
        [sunday] --> Bit 6
        [RESERVED] --> Bit 7 (Default 0)
                                                     
        Example Calculation for every day : 
        day_factor = 0b01111111 = 127
        
        Example Calculation for (sunday + monday + tuesday) :
        day_factor = 0b01000011 = 67

        Returns
        ------- 
        result : int
            "1" for SET_OK, "2" for SET_FAILED 
        """

        value = bytearray()
        value.append(event_id)
        value.append(schedule_type)
        value.append(repeat)
        value.append((time_or_interval >> 24) & 0xFF)
        value.append((time_or_interval >> 16) & 0xFF)
        value.append((time_or_interval >> 8) & 0xFF)
        value.append(time_or_interval & 0xFF)
        value.append(interval_type)
        value.append(repeat_period)
        value.append(action)

        command.create_set_command(
            command.PROTOCOL_COMMAND_CREATE_SCHEDULED_EVENT, value, 10
        )
        command.send_command()
        delay_ms(timeout)
        raw = command.receive_command(COMMAND_SIZE_FOR_UINT8)

        result = raw[PROTOCOL_HEADER_SIZE]
        return result

    def create_scheduled_event_with_event(self, event, timeout=200):
        """
        Function for creating scheduling event
        
        Parameters
        -----------
        event : Event Class Object
            instance of Event class
        timeout : int (optional)
            timeout while receiving the response (default is RESPONSE_DELAY)

        Returns
        ------- 
        result : int
            "1" for SET_OK, "2" for SET_FAILED 
        """

        value = bytearray()
        value.append(event.id)
        value.append(event.schedule_type)
        value.append(event.repeat)
        value.append((event.time_interval >> 24) & 0xFF)
        value.append((event.time_interval >> 16) & 0xFF)
        value.append((event.time_interval >> 8) & 0xFF)
        value.append(event.time_interval & 0xFF)
        value.append(event.interval_type)
        value.append(event.day)
        value.append(event.action)

        command.create_set_command(
            command.PROTOCOL_COMMAND_CREATE_SCHEDULED_EVENT, value, 10
        )
        command.send_command()
        delay_ms(timeout)
        raw = command.receive_command(COMMAND_SIZE_FOR_UINT8)

        result = raw[PROTOCOL_HEADER_SIZE]
        return result

    def get_scheduled_event_ids(self, timeout=50):
        """
        Function for getting scheduled event ids
        
        Parameters
        -----------
        timeout : int (optional)
            timeout while receiving the response (default is RESPONSE_DELAY)

        Returns
        ------- 
        ids : byteArray(10)
            active ids of scheduled events 
        """

        command.create_command(command.PROTOCOL_COMMAND_GET_SCHEDULED_EVENT_IDS)
        command.send_command()
        delay_ms(timeout)
        raw = command.receive_command(COMMAND_SIZE_FOR_INT16)

        ids = int.from_bytes(
            raw[PROTOCOL_HEADER_SIZE : COMMAND_SIZE_FOR_INT16 - 2], "big"
        )
        ids_bytes = bytearray()

        for i in range(10):
            if ids & (1 << i):
                ids_bytes.append(i + 1)
        return ids_bytes

    def remove_scheduled_event(self, event_id, timeout=200):
        """
        Function for removing scheduling event with event id
        
        Parameters
        -----------
        event_id : int
            event id that is required to remove
        timeout : int (optional)
            timeout while receiving the response (default is RESPONSE_DELAY)

        Returns
        ------- 
        result : int
            "1" for SET_OK, "2" for SET_FAILED
        """

        command.create_set_command(
            command.PROTOCOL_COMMAND_REMOVE_SCHEDULED_EVENT, event_id, 1
        )
        command.send_command()
        delay_ms(timeout)
        raw = command.receive_command(COMMAND_SIZE_FOR_UINT8)

        result = raw[PROTOCOL_HEADER_SIZE]
        return result

    def remove_all_scheduled_events(self, timeout=200):
        """
        Function for removing all scheduling events
        
        Parameters
        -----------
        timeout : int (optional)
            timeout while receiving the response (default is RESPONSE_DELAY)

        Returns
        ------- 
        result : int
            "1" for SET_OK, "2" for SET_FAILED
        """

        command.create_command(command.PROTOCOL_COMMAND_REMOVE_ALL_SCHEDULED_EVENTS)
        command.send_command()
        delay_ms(timeout)
        raw = command.receive_command(COMMAND_SIZE_FOR_UINT8)

        result = raw[PROTOCOL_HEADER_SIZE]
        return result

    def get_firmware_ver(self, timeout=RESPONSE_DELAY):
        """
        Function for getting firmware version on mcu
        
        Parameters
        -----------
        timeout : int (optional)
            timeout while receiving the response (default is RESPONSE_DELAY)

        Returns
        ------- 
        version : char[8] 
            ver [Ex. v1.00.00]
        """

        command.create_command(command.PROTOCOL_COMMAND_GET_FIRMWARE_VER)
        command.send_command()
        delay_ms(timeout)
        raw = command.receive_command(15)
        ver = bytearray(8)

        for i in range(8):
            ver[i] = raw[PROTOCOL_HEADER_SIZE + i]

        ver_str = ver.decode("utf-8")
        return ver_str

    def update_firmware(self, firmware_file, update_method=0, timeout=25):
        """
        Function for updating mcu firmware. Do not make any other api call while update call is running.
        
        Parameters
        -----------
        firmware_file : str
            .bin file path
        update_method : int (optional)
            "0" for boot_mode_update, "1" for firmware_mode_update (default is 0)
        timeout : int (optional)
            timeout while receiving the response (default is RESPONSE_DELAY)

        Yields
        ------
        process : int
            Process [%] on every step

        Returns
        ------- 
        result : int
            "1" for SUCCESS, "2" for FAIL
        """

        packet_id = 0
        requesting_packet_id = 1
        packet_size = 20

        # Calculate packet count
        f = open(firmware_file, "rb")
        all_data = f.read()
        leap_packet_size = len(all_data) % packet_size
        packet_count = int(len(all_data) / packet_size) + 1
        
        if leap_packet_size == 0:
             packet_count = int(len(all_data) / packet_size)

        f.close()

        # open file
        f = open(firmware_file, "rb")
        data = bytes()

        # Clear program storage for saving new program data
        result = self.clear_program_storage()
        # print("Program Storage Clear Result: " + str(result))
        if result != 1:
            return Definition.SET_FAILED

        last_process = 0  # for process bar

        # choose the update_method
        if update_method == 0:
            self.reset_for_boot_update()
            delay_ms(800)

        # If any data exist
        while data or (packet_id == 0):
            if packet_id != requesting_packet_id:
                data = f.read(packet_size)
                packet_id += 1

            # calculate the process
            process = int((packet_id * 100) / packet_count)
            yielded_value = None

            if process != last_process:
                if yielded_value != process:
                    yielded_value = process
                    yield process

                last_process = process

            # send data to MCU
            if data:
                if packet_id == packet_count:
                    command.create_firmware_update_command(
                        packet_count,
                        requesting_packet_id,
                        data,
                        packet_len=leap_packet_size,
                    )
                    command.send_command()
                    delay_ms(timeout)
                    raw = command.receive_command(COMMAND_SIZE_FOR_INT16)
                else:
                    command.create_firmware_update_command(
                        packet_count, requesting_packet_id, data
                    )
                    command.send_command()
                    delay_ms(timeout)
                    raw = command.receive_command(COMMAND_SIZE_FOR_INT16)

                try:
                    requesting_packet_id = (raw[5] << 8) | (raw[6] & 0xFF)
                    # print("Last Packet Read --> " + str(packet_id))
                    # print("Requesting --> " + str(requesting_packet_id))

                    # if final packet comes
                    if requesting_packet_id == 0xFFFF:
                        print("Firmware packages are being writen to flash...")
                        print("Please wait until the application starts!")
                        self.reset_mcu()
                        return
                except:
                    raise ValueError("None Object Exception")

        # if firmware update doesn't ended succesfully
        raise RuntimeError("Unidentified Runtime Exception")

    def clear_program_storage(self, timeout=500):
        """
        Function for clearing firmware storage
        
        Parameters
        -----------
        timeout : int (optional)
            timeout while receiving the response (default is RESPONSE_DELAY)

        Returns
        ------- 
        result : int
            "1" for SUCCESS, "2" for FAIL
        """

        command.create_command(command.PROTOCOL_COMMAND_CLEAR_PROGRAM_STORAGE)
        command.send_command()
        delay_ms(timeout)
        raw = command.receive_command(COMMAND_SIZE_FOR_UINT8)

        result = raw[PROTOCOL_HEADER_SIZE]
        return result

    def reset_mcu(self):
        """
        Function for resetting MCU
        
        Parameters
        -----------
        None

        Returns
        ------- 
        None
        """

        command.create_command(command.PROTOCOL_COMMAND_RESET_MCU)
        command.send_command()

    def reset_for_boot_update(self):
        """
        Function for resetting MCU and go to boot mode
        
        Parameters
        -----------
        None

        Returns
        ------- 
        None
        """

        command.create_command(command.PROTOCOL_COMMAND_RESET_MCU_FOR_BOOT_UPDATE)
        command.send_command()

    
    def get_lpm_status(self, timeout=RESPONSE_DELAY):
        """
        Function for getting low power mode status
        
        Parameters
        -----------
        timeout : int (optional)
            timeout while receiving the response (default is RESPONSE_DELAY)

        Returns
        ------- 
        status : int
            "1" for LPM ENABLED, "2" for LPM DISABLED 
        """

        command.create_command(command.PROTOCOL_COMMAND_GET_LOW_POWER_MODE)
        command.send_command()
        delay_ms(timeout)
        raw = command.receive_command(COMMAND_SIZE_FOR_UINT8)

        status = raw[PROTOCOL_HEADER_SIZE]
        return status


    def get_edm_status(self, timeout=RESPONSE_DELAY):
        """
        Function for getting easy deployment mode status
        
        Parameters
        -----------
        timeout : int (optional)
            timeout while receiving the response (default is RESPONSE_DELAY)

        Returns
        ------- 
        status : int
            "1" for EDM ENABLED, "2" for EDM DISABLED 
        """

        command.create_command(command.PROTOCOL_COMMAND_GET_EASY_DEPLOYMENT_MODE)
        command.send_command()
        delay_ms(timeout)
        raw = command.receive_command(COMMAND_SIZE_FOR_UINT8)

        status = raw[PROTOCOL_HEADER_SIZE]
        return status


    def set_lpm_status(self, status, timeout=RESPONSE_DELAY):
        """
        Function for setting low power mode status
        
        Parameters
        -----------
        status : int
            "1" for ENABLED, "2" for DISABLED
        timeout : int (optional)
            timeout while receiving the response (default is RESPONSE_DELAY)

        Returns
        ------- 
        result : int
            "1" for SET OK, "2" for SET FAILED
        """

        command.create_set_command(
            command.PROTOCOL_COMMAND_SET_LOW_POWER_MODE, status, 1
        )
        command.send_command()
        delay_ms(timeout)
        raw = command.receive_command(COMMAND_SIZE_FOR_UINT8)

        status = raw[PROTOCOL_HEADER_SIZE]
        return status


    def set_edm_status(self, status, timeout=RESPONSE_DELAY):
        """
        Function for setting easy deployment mode status
        
        Parameters
        -----------
        status : int
            "1" for ENABLED, "2" for DISABLED
        timeout : int (optional)
            timeout while receiving the response (default is RESPONSE_DELAY)

        Returns
        ------- 
        result : int
            "1" for SET OK, "2" for SET FAILED
        """

        command.create_set_command(
            command.PROTOCOL_COMMAND_SET_EASY_DEPLOYMENT_MODE, status, 1
        )
        command.send_command()
        delay_ms(timeout)
        raw = command.receive_command(COMMAND_SIZE_FOR_UINT8)

        status = raw[PROTOCOL_HEADER_SIZE]
        return status
    
    
    def set_fan_mode(self, mode, timeout=RESPONSE_DELAY):
        """
        Function for setting fan mode
        
        Parameters
        -----------
        status : int
            "1" for FAN ON MODE, "2" for FAN OFF MODE, "3" for FAN AUTO MODE 
        timeout : int (optional)
            timeout while receiving the response (default is RESPONSE_DELAY)

        Returns
        ------- 
        result : int
            "1" for SET OK, "2" for SET FAILED
        """

        command.create_set_command(
            command.PROTOCOL_COMMAND_SET_FAN_MODE, mode, 1
        )
        command.send_command()
        delay_ms(timeout)
        raw = command.receive_command(COMMAND_SIZE_FOR_UINT8)

        status = raw[PROTOCOL_HEADER_SIZE]
        return status


    def get_fan_mode(self, timeout=RESPONSE_DELAY):
        """
        Function for getting fan mode
        
        Parameters
        -----------
        timeout : int (optional)
            timeout while receiving the response (default is RESPONSE_DELAY)

        Returns
        ------- 
        status : int
            "1" for FAN ON MODE, "2" for FAN OFF MODE, "3" for FAN AUTO MODE 
        """

        command.create_command(command.PROTOCOL_COMMAND_GET_FAN_MODE)
        command.send_command()
        delay_ms(timeout)
        raw = command.receive_command(COMMAND_SIZE_FOR_UINT8)

        status = raw[PROTOCOL_HEADER_SIZE]
        return status