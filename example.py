from pms_python_api import SixfabPMS
import time

pms = SixfabPMS()

print(pms.getInputTemp())
time.sleep(0.5)
print(pms.getInputVoltage())
time.sleep(0.5)
print(pms.getInputCurrent())
time.sleep(0.5)
print(pms.getInputPower())
