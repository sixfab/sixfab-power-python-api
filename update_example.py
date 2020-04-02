from pms_api import SixfabPMS, Definition
import time

pms = SixfabPMS()

result = pms.updateFirmware("pms-firmware.bin", timeout=25)
print(result)
