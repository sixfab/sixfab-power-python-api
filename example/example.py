from pms_api import SixfabPMS, Definition
import time

pms = SixfabPMS()

print("System Temp: " + str(pms.getSystemTemp()))
print("System Temp: " + str(pms.sendSystemTemp()))



