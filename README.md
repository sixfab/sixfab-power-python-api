# Sixfab Power Python API

Sixfab Power API is offered for the UPS HAT v2 for easy integration into the user's project. 

PS. This API is strictly for Sixfab UPS HAT v2. Sixfab UPS HAT v1 users should follow [UPS HAT V1 API](https://github.com/sixfab/sixfab-power-python-api/tree/UPS_HAT_V1).

Before we install the API, enable the I2C of the Raspberry Pi as the Sixfab UPS HAT v2 and the RPi communicates over the I2C. 

To enable it run 
```sudo raspi-config``` 
and navigate to **Interfacing Options >> I2C**. Select **YES** as the answer of the question **"Would you like the ARM I2C interface to be enabled?**


## Installation

If you don't have the pip3 install on your Raspberry Pi install it pip3:

```sudo apt -y install python3-pip```


Now run the following command to install the API. 

```pip3 install power-api```

## Upgrade

The API can be upgraded to the latest package if available. 

```pip3 install power-api --upgrade```

## Uninstall 

Installed API package can be uninstalled uysing the following ccommand.

```pip3 uninstall power-api```

## Usage
#### Example Codes

Here are some [example](./example) codes that has been prepared the Python API. 

* [create_event.py](./example/create_event.py)
* [read_sensors.py](./example/read_sensors.py)
* [reset_mcu.py](./example/reset_mcu.py)
* [rtc_set.py](./example/rtc_set.py)
* [rtc_time.py](./example/rtc_time.py)
* [update_firmware.py](./example/update_firmware.py) 

## API Docs
[API Docs](https://sixfab.github.io/sixfab-power-python-api/)
