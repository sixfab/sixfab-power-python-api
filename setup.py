from setuptools import setup, find_packages

setup(
    name='sixfab_pms',
    version='0.0.1',
    author='Yasin Kaya',
    author_email='yasinkaya.121@gmail.com',
    description='Sixfab power management service python api',
    license='MIT',
    url='https://github.com/sixfab/pms-python-api',
    dependency_links  = [],
    install_requires  = ['smbus2'],
	packages=find_packages()
)
