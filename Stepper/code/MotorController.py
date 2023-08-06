import time
from CurtainState import CurtainState
import RPi.GPIO as GPIO

class MotorController:
    def __init__(self, state: CurtainState, stepPin, dirPin, enablePin, ms1, ms2, ms3, rst, slp) -> None:
        self.state = state
        self.stepPin = stepPin
        self.dirPin = dirPin
        self.enablePin = enablePin
        self.ms1 = ms1
        self.ms2 = ms2
        self.ms3 = ms3
        self.rst = rst
        self.slp = slp
        self.speed = 0.1

        GPIO.setup(stepPin, GPIO.OUT)
        GPIO.setup(dirPin, GPIO.OUT)
        GPIO.setup(enablePin, GPIO.OUT)
        GPIO.setup(slp, GPIO.OUT)
        GPIO.setup(rst, GPIO.OUT)
        GPIO.setup(ms1, GPIO.OUT)
        GPIO.setup(ms2, GPIO.OUT)
        GPIO.setup(ms3, GPIO.OUT)
        GPIO.setup(slp, GPIO.OUT)
        GPIO.setup(rst, GPIO.OUT)

        GPIO.output(enablePin, 1)
        GPIO.output(slp, 1)
        GPIO.output(rst, 1)
        GPIO.output(ms1, 0)
        GPIO.output(ms2, 0)
        GPIO.output(ms3, 0)

    def step(self, pulseLength):
        GPIO.output(self.slp, 1)
        GPIO.output(self.stepPin, 1)
        time.sleep(self.speed/2)
        GPIO.output(self.stepPin, 0)
        time.sleep(self.speed/2)
        self.speed -= (self.speed - pulseLength) / 20
        self.speed = max(pulseLength, self.speed)
        print(self.speed)

    def getStep(self):
        return GPIO.input(self.stepPin)

    def enable(self):
        GPIO.output(self.enablePin, 0)

    def disable(self):
        GPIO.output(self.enablePin, 1)

    def setDirection(self, direction):
        GPIO.output(self.dirPin, direction)

    def reset(self):
        GPIO.output(self.rst, 0)
        time.sleep(0.01)
        GPIO.output(self.rst, 1)
        
    def sleep(self):
        GPIO.output(self.slp, 0)

    def update(self):
        if self.state.targetPosition > self.state.position and self.state.canClose():
            self.setDirection(1)
            self.step(self.state.speed)
            self.state.position += 1
        elif self.state.targetPosition < self.state.position and self.state.canOpen():
            self.setDirection(0)
            self.step(self.state.speed)
            self.state.position -= 1
        else:
            self.sleep()
            time.sleep(0.01)
            self.speed = 0.1
        