import CurtainState
from Pins import Pins
from RPi import GPIO
from MotorController import MotorController
from Screen import Screen
from threading import Thread
import time
from PhysicalInput import PhysicalInput
from Screens.ScreenInterpreter import ScreenInterpreter
from Screens.MainScreen import MainScreen
from AutomationManager import AutomationManager

GPIO.setmode(GPIO.BCM)

pins = Pins()
state = CurtainState.CurtainState()
physicalInput = PhysicalInput(pins.rotaryA.get(), pins.rotaryB.get(), pins.rotaryButton.get(), pins.btnL.get(), pins.btnR.get())
motorController = MotorController(state, pins.step.get(), pins.dir.get(), pins.enable.get(), pins.m0.get(), pins.m1.get(), pins.m2.get(), pins.reset.get(), pins.sleep.get())
screen = Screen()
screenInterpreter = ScreenInterpreter(screen, physicalInput)
screenInterpreter.setScreen(MainScreen(screenInterpreter.setScreen))
automation = AutomationManager(state)


def motorLoop():
    while True:
        motorController.update()

def automationLoop():
    while True:
        automation.update()

def controlLoop():
    while True:
        screenInterpreter.update()
        time.sleep(0.01)


motorThread = Thread(target = motorLoop)
controlThread = Thread(target = controlLoop)
automationThread = Thread(target = automationLoop)

motorThread.start()
controlThread.start()
automationThread.start()