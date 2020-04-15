from pms_api import SixfabPMS, Definition
import time

pms = SixfabPMS()

print("System Temp: " + str(pms.getBatteryLevel()))



