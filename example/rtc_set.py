from power_api import SixfabPower, Definition, Event
import time

api = SixfabPower()

epoch = time.time() # to get timestamp in seconds in GMT0

# to get local time on raspberry pi 
localtime = time.asctime( time.localtime(time.time()) )
print("Local current time :", localtime)

# to get timezone difference as minus 
print(time.timezone)

# standard epoch time with no location specific
print("Epoch Time: " + str(int(epoch)))

# to calculate epoch with respect to local time
# use it for set_rtc_time() function as timestamp (epoch - time.timezone)
print("Epoch Local: " + str(int(epoch) - time.timezone))
print("Result: " + str(api.set_rtc_time(int(epoch) - time.timezone)))