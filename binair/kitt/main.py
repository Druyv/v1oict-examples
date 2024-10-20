from machine import Pin
import time

led_pins = [
    Pin(11, Pin.OUT),
    Pin(12, Pin.OUT),
    Pin(13, Pin.OUT),
    Pin(14, Pin.OUT),
    Pin(15, Pin.OUT)
]


def leds(value, delay_time):
    for led_pin in led_pins:
        if value % 2 == 1:
            led_pin.on()
        else:
            led_pin.off()
        value = value // 2
    time.sleep(delay_time)


delay = 0.1
while True:
    leds(1, delay)
    leds(2, delay)
    leds(4, delay)
    leds(8, delay)
    leds(16, delay)
