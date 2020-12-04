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
print( "Return: " + str(api.set_watchdog_status(2)))
print( "WDT Status: " + str(api.get_watchdog_status()))

print( "Return: " + str(api.set_watchdog_interval(2)))
print( "WDT Interval: " + str(api.get_watchdog_interval()))

print( "Return: " + str(api.set_fan_mode(2)))
print( "Fan Mode: " + str(api.get_fan_mode()))

print( "Return: " + str(api.set_battery_separation_status(1)))
print( "Battery Separation: " + str(api.get_battery_separation_status()))
"""

#print( "Battery Separation --> Send battery temp result: " + str(api.send_battery_temp()))

"""
print( "Return: " + str(api.set_rgb_animation(2,7,3)))
print( "RGB Anim: " + str(api.get_rgb_animation()))
"""

print( "Return: " + str(api.set_fan_automation(50)))
print( "Fan Automation: " + str(api.get_fan_automation()))