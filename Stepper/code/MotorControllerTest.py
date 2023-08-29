import CurtainState
from Pins import Pins
from RPi import GPIO
from MotorController import MotorController
from threading import Thread

pins = Pins()
state = CurtainState.CurtainState()
motorController = MotorController(state, pins.step.get(), pins.dir.get(), pins.enable.get(), pins.m0.get(), pins.m1.get(), pins.m2.get(), pins.reset.get(), pins.sleep.get())

state.setTargetPosition(10)

def motorLoop():
    while True:
        motorController.update()

motorThread = Thread(target=motorLoop)

motorThread = Thread(target=motorLoop)

motorThread.start()