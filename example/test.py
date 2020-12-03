from power_api import SixfabPower, Definition, Event
import time

api = SixfabPower()

"""
print( "Return: " + str(api.set_lpm_status(2)))
print( "LPM: " + str(api.get_lpm_status()))

print( "Return: " + str(api.set_fan_mode(1)))
print( "LPM: " + str(api.get_fan_mode()))

print( "Battery Temp: " + str(api.get_battery_temp_qwiic()))
"""

"""
print( "Return: " + str(api.set_watchdog_status(1)))
print( "WDT Status: " + str(api.get_watchdog_status()))
"""

print( "Return: " + str(api.set_watchdog_interval(5)))
print( "WDT Interval: " + str(api.get_watchdog_interval()))
