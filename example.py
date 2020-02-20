from pms_python_api import SixfabPMS
import time

pms = SixfabPMS()

print(pms.getBatteryTemp())
time.sleep(0.5)
print(pms.getSystemVoltage())
time.sleep(0.5)
print(pms.getBatteryCurrent())
time.sleep(0.5)
print(pms.getInputPower())
