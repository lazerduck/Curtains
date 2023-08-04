from CurtainState import CurtainState
from Pins import Pins
from RPi import GPIO
from MotorController import MotorController
from RotaryDriver.RotaryDriver import RotaryDriver
from Screen import Screen
from threading import Thread
import time

GPIO.setmode(GPIO.BCM)

pins = Pins()

motorController = MotorController(pins.step.get(), pins.dir.get(), pins.enable.get(), pins.m0.get(), pins.m1.get(), pins.m2.get(), pins.reset.get(), pins.sleep.get())
state = CurtainState()
rotaryDriver = RotaryDriver(pins.rotaryB.get(), pins.rotaryA.get(), pins.rotaryButton.get())
screen = Screen()

def motorLoop():
    while True:
        if state.targetPosition > state.position and state.canClose():
            motorController.setDirection(1)
            motorController.step(state.speed)
            state.position += 1
            print("step left")
        elif state.targetPosition < state.position and state.canOpen():
            motorController.setDirection(0)
            motorController.step(state.speed)
            state.position -= 1
            print("step right")
        else:
            time.sleep(0.01)
            print("skip step")

def test():
    print("resetting")
    motorController.reset()

rotaryDriver.buttonEvent = test

def controlLoop():
    while True:
        state.setTargetPosition(rotaryDriver.pos*100)
        screen.line2 = str(state.position)
        time.sleep(0.01)


motorThread = Thread(target = motorLoop)
controlThread = Thread(target = controlLoop)

motorThread.start()
controlThread.start()