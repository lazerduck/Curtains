from cmath import pi
from multiprocessing.sharedctypes import Value
from tracemalloc import stop
import RPi.GPIO as GPIO
import threading

class Pin:
    Pin: int
    Value: int

    def __init__(self, pin, value):
        self.Pin = pin
        self.Value = value

class CurtainState:
    open: Pin = Pin(11, False)
    move: Pin = Pin(7, False)
    openTime: int = 26
    closeTime: int = 26

class Curtains:
    state = CurtainState()

    def __init__(self):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.state.move.Pin, GPIO.OUT)
        GPIO.setup(self.state.open.Pin, GPIO.OUT)
        self.timer = threading.Timer(0, self.stop)

    def __del__(self):
        GPIO.cleanup()

    def applyPins(self):
        print("Applying Pins")
        # GPIO.output(self.state.open.Pin, 1 if self.state.open.Value else 0)
        # GPIO.output(self.state.move.Pin, 1 if self.state.move.Value else 0)

    def setOpen(self, value):
        self.state.open.Value = value

    def setMoving(self, value):
        self.state.move.Value = value

    def stop(self):
        print("Stop")
        self.setMoving(False)
        self.setOpen(False)
        self.applyPins()

    def open(self):
        self.setOpen(True)
        self.setMoving(True)
        self.applyPins()
        self.timer.cancel()
        self.timer = threading.Timer(self.state.openTime, self.stop)
        self.timer.start()

    def close(self):
        print("Close")
        self.setOpen(False)
        self.setMoving(True)
        self.applyPins()
        self.timer.cancel()
        self.timer = threading.Timer(self.state.closeTime, self.stop)
        self.timer.start()

    def getState(self):
        return self.state

    def setOpenTime(self, time):
        self.state.openTime = time

    def setCloseTime(self, time):
        self.state.closeTime = time
