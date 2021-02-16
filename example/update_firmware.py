from power_api import SixfabPower
import time
import sys
import os

api = SixfabPower()

firmware_path = "./firmwares/sixfab_pms_firmware_v0.3.3.bin"

error_occurred = 0
try:
    for step in api.update_firmware(firmware_path):
        print(f"{step}%")

except:
    error_occurred = 1
    print("raised error")

finally:
    update_successful = 0
    if error_occurred == 0:
        counter = 0

        for i in range(15):
            print('.', sep=' ', end=' ', flush=True)
            time.sleep(1)

        while(1):
            try:
                sys.stdout = open(os.devnull, 'w')
                fw_ver = api.get_firmware_ver()
                sys.stdout = sys.__stdout__
            except:
                counter += 1
                print('.', sep=' ', end=' ', flush=True)
            else:
                update_successful = 1
            finally:
                if update_successful == 1:
                    print("\nUpdate is Successful to FW Ver: " + str(fw_ver))
                    break
                else:
                    if counter >= 10:
                        print("Update is Failed!")
                        break

            time.sleep(2)
