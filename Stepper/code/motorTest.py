from Pins import Pins
from RPi import GPIO
import time

class StepperMotor:
    def __init__(self, enable_pin, step_pin, dir_pin, mode_pins, step_type, fullstep_delay):
        """docstring for ."""
        self.enable_pin = enable_pin
        self.step_pin = step_pin
        self.dir_pin = dir_pin
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(enable_pin, GPIO.OUT)
        GPIO.setup(step_pin, GPIO.OUT)
        GPIO.setup(dir_pin, GPIO.OUT)
        GPIO.setup(mode_pins, GPIO.OUT)
        resolution = {'Full':(0, 0, 0),
                    'Half':(1, 0, 0),
                    '1/4':(0, 1, 0),
                    '1/8':(1, 1, 0),
                    '1/16':(0, 0, 1),
                    '1/32':(1, 0, 1)}
        microsteps =  {'Full':1,
                    'Half':2,
                    '1/4':4,
                    '1/8':8,
                    '1/16':16,
                    '1/32':32}
        self.delay = fullstep_delay/microsteps[step_type]
        GPIO.output(mode_pins, resolution[step_type])

    def enable(self, enable):
        GPIO.output(self.enable_pin, not enable)

    def run(self, steps, clockwise):
        GPIO.output(self.dir_pin, clockwise)
        for i in range(steps):
            GPIO.output(self.step_pin, GPIO.HIGH)
            time.sleep(self.delay)
            GPIO.output(self.step_pin, GPIO.LOW)
            time.sleep(self.delay)


GPIO.setmode(GPIO.BCM)

pins = Pins()

motor = StepperMotor(pins.enable.get(), pins.step.get(), pins.dir.get(), (pins.m0.get(), pins.m1.get(), pins.m2.get()), 'Full', 0.05)


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