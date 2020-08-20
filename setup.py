from setuptools import setup, find_packages

setup(
    name='sixfab-power-python-api',
    version='0.1.0',
    author='Yasin Kaya',
    author_email='yasinkaya.121@gmail.com',
    description='Sixfab power management service python api',
    license='MIT',
    url='https://github.com/sixfab/sixfab-power-python-api',
    dependency_links  = [],
    install_requires  = ['smbus2==0.3.0', 'crc16==0.1.1'],
	packages=find_packages()
)
