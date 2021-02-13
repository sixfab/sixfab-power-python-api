from power_api import SixfabPower, Definition, Event
import time

api = SixfabPower()


#print( "Return: " + str(api.set_lpm_status(2)))
print( "LPM: " + str(api.get_lpm_status()))

#print( "Battery Temp: " + str(api.get_battery_temp_qwiic()))

#print( "Return: " + str(api.set_watchdog_status(2)))
print( "WDT Status: " + str(api.get_watchdog_status()))

#print( "Return: " + str(api.set_watchdog_interval(2)))
print( "WDT Interval: " + str(api.get_watchdog_interval()))

#print( "Return: " + str(api.set_fan_mode(2)))
print( "Fan Mode: " + str(api.get_fan_mode()))

#print( "Return: " + str(api.set_battery_separation_status(1)))
print( "Battery Separation: " + str(api.get_battery_separation_status()))

#print( "Return: " + str(api.set_rgb_animation(2,7,3)))
print( "RGB Anim: " + str(api.get_rgb_animation()))

#print( "Return: " + str(api.set_fan_automation(50)))

#print( "Return: " + str(api.set_power_outage_event_status(1)))
print( "POWER OUT. STAT: " + str(api.get_power_outage_event_status()))

#print( "Return: " + str(api.set_power_outage_params(5,30)))
print( "POWER OUT. PARAMS: " + str(api.get_power_outage_params()))

#print( "Return: " + str(api.set_end_device_alive_threshold(250)))
print( "Alive Threshold: " + str(api.get_end_device_alive_threshold()))

print( "EDM: " + str(api.get_edm_status()))

print( "LPM: " + str(api.get_lpm_status()))

print( "WDT INTERVAL: " + str(api.get_watchdog_interval()))

print( "Power Outage Status: " + str(api.get_power_outage_event_status()))

print( "SE ID's: " + str(api.get_scheduled_event_ids()))

#print( "Factory Reset: " + str(api.restore_factory_defaults()))
