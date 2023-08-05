from CurtainState import CurtainState
from Pins import Pins
from RPi import GPIO
from MotorController import MotorController
from Screen import Screen
from threading import Thread
import time
import keyboard

from PhysicalInput import PhysicalInput

GPIO.setmode(GPIO.BCM)

pins = Pins()
state = CurtainState()
physicalInput = PhysicalInput(pins.rotaryA.get(), pins.rotaryB.get(), pins.rotaryButton.get(), pins.buttonL.get(), pins.buttonR.get())
motorController = MotorController(state, pins.step.get(), pins.dir.get(), pins.enable.get(), pins.m0.get(), pins.m1.get(), pins.m2.get(), pins.reset.get(), pins.sleep.get())
screen = Screen()

def motorLoop():
    while True:
        motorController.update()

def controlLoop():
    if keyboard.is_pressed('q'):  # if key 'q' is pressed 
        print('key')
        physicalInput.rotaryDriver.pos += 1
    state.setTargetPosition(physicalInput.getRotation())
    screen.line2 = str(state.position)
    time.sleep(0.01)


motorThread = Thread(target = motorLoop)
controlThread = Thread(target = controlLoop)

motorThread.start()
controlThread.start()