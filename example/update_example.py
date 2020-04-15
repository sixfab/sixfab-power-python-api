from pms_api import SixfabPMS, Definition
import time

pms = SixfabPMS()

result = 2 # failed by default

try:
    for step in pms.updateFirmware("pms-firmware.bin"):
        print(f"{step}%")

    print(f"Process ended with status code {result}")
except:
    print("raised error")