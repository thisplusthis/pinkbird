"""
    Check Humidity via DHT-22 and toggle 4 channel relay
    to turn fan on for a set number of seconds before
    turning back off again.
"""

import time

import Adafruit_DHT
import RPi.GPIO as GPIO

from django.core.management.base import BaseCommand

from pinkbird.models import Reading

# constants
DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4
FAN_DURATION = 6
HUMIDITY_LOW = 85.0
READ_DELAY = 5
PIN_LOOKUPS = {
    18: GPIO.OUT,
    23: GPIO.OUT,
    24: GPIO.OUT,
    25: GPIO.OUT,
}


class Command(BaseCommand):
    help = """Get readings from DHT-22 and log them to the django database"""

    def setup_gpio(self):
        """
        Setup relay pins
        """
        # The script as below using BCM GPIO 00..nn numbers
        GPIO.setmode(GPIO.BCM)

        # Set relay pins as output
        for pin, setting in PIN_LOOKUPS.items():
            GPIO.setup(pin, setting)

    def toggle_relay(self, state):
        """
        Turn on/off to control AC unit
        :param state: LOW / HIGH
        """
        on_off = GPIO.HIGH if state else GPIO.LOW
        for pin in PIN_LOOKUPS.keys():
            GPIO.output(pin, on_off)

    def log_readings(self, humidity, temp):
        """
        :param humidity:
        :param temp:
        :return:
        """

        reading = Reading(temperature=float(temp), humidity=float(humidity))
        reading.save()

        if humidity <= HUMIDITY_LOW:
            self.toggle_relay(True)
            reading.fan = True
            reading.save()
            time.sleep(FAN_DURATION)  # turn fan on for 'n' seconds
            self.toggle_relay(False)

    def handle(self, *args, **kwargs):
        self.setup_gpio()
        while True:
            humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
            self.log_readings(humidity, temperature)
            time.sleep(READ_DELAY)
