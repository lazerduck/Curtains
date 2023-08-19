from Pins import Pins
from RPi import GPIO
import time
from rpi_python_drv8825.stepper import StepperMotor

GPIO.setmode(GPIO.BCM)

pins = Pins()

motor = StepperMotor(pins.enable.get(), pins.step.get(), pins.dir.get(), (pins.m0.get(), pins.m1.get(), pins.m2.get()), 'Full', 0.005)


GPIO.setup(pins.enable.get(), GPIO.OUT)
GPIO.setup(pins.sleep.get(), GPIO.OUT)
GPIO.setup(pins.reset.get(), GPIO.OUT)
GPIO.output(pins.enable.get(), 1)
GPIO.output(pins.sleep.get(), 1)
GPIO.output(pins.reset.get(), 1)

motor.enable(True)        # enables stepper driver
motor.run(640, True)     # run motor 6400 steps clowckwise
motor.run(640, False)    # run motor 6400 steps counterclockwise
motor.enable(False) 

GPIO.output(pins.sleep.get(), 0)

GPIO.cleanup()