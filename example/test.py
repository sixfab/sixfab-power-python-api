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
"""

#print( "Return: " + str(api.set_battery_separation_status(1)))
#print( "Battery Separation: " + str(api.get_battery_separation_status()))

#print( "Battery Separation --> Send battery temp result: " + str(api.send_battery_temp()))

"""
print( "Return: " + str(api.set_rgb_animation(2,7,3)))
print( "RGB Anim: " + str(api.get_rgb_animation()))
"""
"""
print( "Return: " + str(api.set_fan_automation(50)))

fan = api.get_fan_automation()
print( "Fan Automation: " + str(fan[0]))
"""

"""
# Setter limit test
print( "WDT: " + str(api.set_watchdog_status(1)))
print( "RGB: " + str(api.set_rgb_animation(2,1,3)))
print( "FAN: " + str(api.set_fan_automation(50)))
print( "BAT. MAX: " + str(api.set_battery_max_charge_level(100)))
print( "BAT. SAFE: " + str(api.set_safe_shutdown_battery_level(1)))
print( "BAT SAFE STAT: " + str(api.set_safe_shutdown_status(1)))
print( "SEPARATION: " + str(api.set_battery_separation_status(1)))
print( "BAT CAP: " + str(api.set_battery_design_capacity(2500)))
print( "BAT CAP: " + str(api.set_watchdog_interval(2)))
"""

"""
print( "Return: " + str(api.set_power_outage_event_status(1)))
print( "POWER OUT. STAT: " + str(api.get_power_outage_event_status()))

print( "Return: " + str(api.set_power_outage_params(5,30)))
print( "POWER OUT. PARAMS: " + str(api.get_power_outage_params()))
"""
print( "Alive Threshold: " + str(api.get_end_device_alive_threshold()))
print( "Return: " + str(api.set_end_device_alive_threshold(250)))
print( "Alive Threshold: " + str(api.get_end_device_alive_threshold()))