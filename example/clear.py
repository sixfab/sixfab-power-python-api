from pms_api import SixfabPMS, Definition
import time

pms = SixfabPMS()

print("Clear " + str(pms.clearPipe()))