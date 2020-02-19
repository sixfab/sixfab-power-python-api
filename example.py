from pms-python-api import SixfabPMS

pms = SixfabPMS()

print(pms.getInputTemp())
delay_ms(500)
print(pms.getInputVoltage())
delay_ms(500)
print(pms.getInputCurrent())
delay_ms(500)
print(pms.getInputPower())
