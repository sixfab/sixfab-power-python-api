from power_api import SixfabPower, Definition
import time

api = SixfabPower()

firmware_path = "sixfab_pms_firmware_vx.y.z.bin"

try:
    for step in api.update_firmware(firmware_path):
        print(f"{step}%")

except:
    print("raised error")