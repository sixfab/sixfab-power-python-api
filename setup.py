import os
from setuptools import setup, find_packages
import subprocess


def install_request_distribution_service():
    if os.getuid() != 0 and not os.path.exists("/opt/sixfab/pms/api"):
        # root privileges not exists, skip the installation of request service
        return

    print("""============================================================================""")
    print("Installing service")

    try:
        null = open("/dev/null", "w")
        subprocess.Popen("git", stdout=null, stderr=null)
        null.close()

    except OSError:
        print("Git not found, installing git")
        os.system("apt update && apt-get -y install git")

    directories = (
        "/opt/sixfab",
        "/opt/sixfab/pms",
        "/opt/sixfab/pms/api"
    )

    for directory in directories:
        if not os.path.exists(directory):
            os.mkdir(directory)

    os.system("git clone --quiet https://github.com/sixfab/power_distribution-service.git /opt/sixfab/pms/api  > /dev/null 2>&1")

    os.system("pip3 install -r /opt/sixfab/pms/api/requirements.txt > /dev/null 2>&1")

    with open("/etc/systemd/system/power_request.service", "w") as service_file:
        service_file.write("""[Unit]
Description=Sixfab UPS HAT Distributed API

[Service]
User=pi
ExecStart=/usr/bin/python3 /opt/sixfab/pms/api/run_server.py

[Install]
WantedBy=multi-user.target""")

    os.system("""
        sudo systemctl daemon-reload &&
        sudo systemctl enable power_request > /dev/null 2>&1 &&
        sudo systemctl start power_request
    """)

    print("Service finished, please visit http://localhost:6060/docs for documentation")

setup(
    name='sixfab-power-python-api',
    version='0.2.1',
    author='Yasin Kaya',
    author_email='yasinkaya.121@gmail.com',
    description='Sixfab power management service python api',
    license='MIT',
    url='https://github.com/sixfab/sixfab-power-python-api',
    dependency_links  = [],
    install_requires  = ['smbus2==0.3.0', 'crc16==0.1.1', 'vcgencmd==0.1.1'],
	packages=find_packages()
)

install_request_distribution_service()