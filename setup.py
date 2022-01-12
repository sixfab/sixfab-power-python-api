from setuptools import setup, find_packages

setup(
    name='power_api',
    version='0.3.2',
    author='Yasin Kaya',
    author_email='yasinkaya.121@gmail.com',
    description='Python API for Sixfab UPS HAT V2',
    license='MIT',
    url='https://github.com/sixfab/sixfab-power-python-api',
    dependency_links  = [],
    install_requires  = ['smbus2==0.3.0', 'crc16==0.1.1', 'vcgencmd==0.1.1'],
    packages=find_packages()
)