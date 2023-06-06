import time
from CurtainState import CurtainState
import RPi.GPIO as GPIO

class MotorController:
    def __init__(self, stepPin, dirPin, enablePin, ms1, ms2, ms3) -> None:
        self.stepPin = stepPin
        self.dirPin = dirPin
        self.enablePin = enablePin
        self.ms1 = ms1
        self.ms2 = ms2
        self.ms3 = ms3

        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(stepPin, GPIO.OUT)
        GPIO.setup(dirPin, GPIO.OUT)
        GPIO.setup(enablePin, GPIO.OUT)
        GPIO.setup(ms1, GPIO.OUT)
        GPIO.setup(ms2, GPIO.OUT)
        GPIO.setup(ms3, GPIO.OUT)

        GPIO.output(enablePin, 1)
        GPIO.output(ms1, 0)
        GPIO.output(ms2, 0)
        GPIO.output(ms3, 0)

    def step(self, pulseLength):
        GPIO.output(self.stepPin, 1)
        time.sleep(pulseLength/2)
        GPIO.output(self.stepPin, 0)
        time.sleep(pulseLength/2)

    def enable(self):
        GPIO.output(self.enablePin, 0)

    def disable(self):
        GPIO.output(self.enablePin, 1)

    def setDirection(self, direction):
        GPIO.output(self.dirPin, direction)
        