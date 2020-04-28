from pms_api import pms_api, Definition
import time

pms = SixfabPMS()

print("Clear " + str(pms.clearPipe()))