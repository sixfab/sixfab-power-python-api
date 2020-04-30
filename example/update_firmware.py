from power_api import SixfabPower, Definition
import time

api = SixfabPower()

result = 2 # failed by default

firmware_path = "pms-firmware.bin"

try:
    for step in api.update_firmware(firmware_path):
        print(f"{step}%")

    print(f"Process ended with status code {result}")
except:
    print("raised error")