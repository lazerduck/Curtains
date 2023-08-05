from Pins import Pins
from RPi import GPIO
import time

GPIO.setmode(GPIO.BCM)

pins = Pins()

GPIO.setup(pins.step.get(), GPIO.OUT)
GPIO.setup(pins.dir.get(), GPIO.OUT)
GPIO.setup(pins.enable.get(), GPIO.OUT)
GPIO.setup(pins.sleep.get(), GPIO.OUT)
GPIO.setup(pins.reset.get(), GPIO.OUT)
GPIO.output(pins.enable.get(), 1)
GPIO.output(pins.sleep.get(), 1)
GPIO.output(pins.reset.get(), 1)

p = GPIO.PWM(pins.step.get(), 100)
p.start(50)

time.sleep(10)

GPIO.cleanup()