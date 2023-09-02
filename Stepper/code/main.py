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

GPIO.setmode(GPIO.BCM)

pins = Pins()
state = CurtainState.CurtainState()
physicalInput = PhysicalInput(pins.rotaryA.get(), pins.rotaryB.get(), pins.rotaryButton.get(), pins.btnL.get(), pins.btnR.get())
motorController = MotorController(state, pins.step.get(), pins.dir.get(), pins.enable.get(), pins.m0.get(), pins.m1.get(), pins.m2.get(), pins.reset.get(), pins.sleep.get())
screen = Screen()
screenInterpreter = ScreenInterpreter(screen, physicalInput)
screenInterpreter.setScreen(MainScreen())


def motorLoop():
    while True:
        motorController.update()

def controlLoop():
    while True:
        state.setTargetPosition(physicalInput.getRotaryPos()*state.stepMultiplier)
        # screen.line2 = "Target: " + str(state.targetPosition)
        # screen.line3 = "Pos: " + str(state.position)
        time.sleep(0.01)


motorThread = Thread(target = motorLoop)
controlThread = Thread(target = controlLoop)

motorThread.start()
controlThread.start()