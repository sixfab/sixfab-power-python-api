from pms_api import SixfabPMS, Definition, Event
import time

pms = SixfabPMS()

#print(pms.getButton1Status())
print(pms.anySoftActionIsExist())