from pms_api import SixfabPMS, Definition
import time

pms = SixfabPMS()

pms.updateFirmware("pms-firmware.bin")