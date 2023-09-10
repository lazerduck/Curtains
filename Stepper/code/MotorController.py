import time
from CurtainState import CurtainState
import RPi.GPIO as GPIO
from MotorDriver.MotorDriver import MotorDriver

class MotorController:
    def __init__(self, state: CurtainState, stepPin, dirPin, enablePin, ms1, ms2, ms3, rst, slp) -> None:
        self.state = state
        self.driver = MotorDriver(stepPin, dirPin, (ms1, ms2, ms3), '1/16', state.speed)
        self.enablePin = enablePin
        self.rst = rst
        self.slp = slp

        GPIO.setup(enablePin, GPIO.OUT)
        GPIO.setup(slp, GPIO.OUT)
        GPIO.setup(rst, GPIO.OUT)

        GPIO.output(enablePin, 1)
        GPIO.output(slp, 1)
        GPIO.output(rst, 1)

    def enable(self):
        GPIO.output(self.enablePin, 0)

    def disable(self):
        GPIO.output(self.enablePin, 1)

    def reset(self):
        GPIO.output(self.rst, 0)
        time.sleep(0.01)
        GPIO.output(self.rst, 1)
        
    def sleep(self):
        GPIO.output(self.slp, 0)

    def wake(self):
        GPIO.output(self.slp, 1)

    def update(self):
        if self.state.targetPosition > self.state.position and self.state.canClose():
            self.wake()
            self.driver.step(16, 1)
            self.state.position += 1
        elif self.state.targetPosition < self.state.position and self.state.canOpen():
            self.wake()
            self.driver.step(16, 0)
            self.state.position -= 1
        else:
            self.sleep()
            time.sleep(0.01)
            self.speed = self.state.startSpeed
        