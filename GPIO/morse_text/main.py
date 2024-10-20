from machine import Pin
import time

morse_code = {
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "i": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...-",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--..",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "0": "-----"
}

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


def morse(pin, dot_length, text):
    """
    Laat de text horen als morse code.
    De pin_nr is de pin die gebruikt wordt.
    De text mag de volgende characters bevatten: spatie, streepje, punt.
    De dot_length is de lengte van een punt (dot).
    De lengte van de andere characters wordt daar van afgeleid.
    """
    for char in text:
        if char == ".":
            pulse(pin, dot_length, dot_length)
        elif char == "-":
            pulse(pin, 2 * dot_length, dot_length)
        elif char == " ":
            time.sleep(2 * dot_length)

def morse_text(pin, dot_length, text):
    """
    Laat de string s horen als morse code.
    De pin_nr is de pin die gebruikt wordt.
    De text mag de volgende characters bevatten: lowercase letters, spatie.
    De dot_length is de lengte van een punt (dot).
    De lengte van de andere characters wordt daar van afgeleid.
    """
    morse_string = ""
    for char in text.lower():
        if char == " ":
            morse_string += " "
        else:
            morse_string += morse_code[char]
    morse(pin, dot_length, morse_string)

morse_text(gpio_pin, 0.2, "Hello world")
