from machine import Pin
import time

gpio_pin = Pin("LED", Pin.OUT)


def pulse(pin, high_time, low_time):
    """
    Geef een puls op de pin:
    Maak de pin pin_nr hoog, wacht high_time,
    maak de pin laag, en wacht nog low_time
    """
    pin.high()
    time.sleep(high_time)
    pin.low()
    time.sleep(low_time)


while True:
    pulse(gpio_pin, 0.2, 0.2)
