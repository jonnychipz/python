import machine
import utime

pin = machine.Pin(25, machine.Pin.OUT)

while True:
    pin.value(1)
    utime.sleep(0.5)
    pin.value(0)
    utime.sleep(0.5)