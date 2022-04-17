import RPi.GPIO as GPIO
import threading
from LightSensor import LightContorl
# from ButtonControl import ButtonControl
from collections import namedtuple
import json
Pin = namedtuple('Pin', 'pin value')
Data = namedtuple('Data', 'isMoving isLeft isBright')

class MotorControl:
    isMovingPin = Pin(7, False)
    isLeftPin = Pin(11, False)
    openTime = 32
    closeTime = 32

    def __init__(self):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.isMovingPin.pin, GPIO.OUT)
        GPIO.setup(self.isLeftPin.pin, GPIO.OUT)
        self.setMoving(False)
        self.setLeft(False)
        self.light = LightContorl(self.doAction)
        self.stopTimer = threading.Timer(10, self.stop)
        #self.buttonCon = ButtonControl(self.startOpen, self.startClose, self.stop)

    def __del__(self):
        GPIO.cleanup()


    def setMoving(self, isMoving):
        self.isMovingPin = Pin(self.isMovingPin.pin, isMoving)
        self.outputPin(self.isMovingPin)
    
    def setLeft(self, isLeft):
        self.isLeftPin = Pin(self.isLeftPin.pin, isLeft)
        self.outputPin(self.isLeftPin)
        
    def outputPin(self, pinObj):
        print("setting " + str(pinObj.pin) + " to " + str(pinObj.value))
        GPIO.output(pinObj.pin, 1 if pinObj.value else 0)

    def doAction(self, isClose):
        self.setMoving(True)
        self.setLeft(isClose)
        self.stopTimer.cancel()
        self.stopTimer = threading.Timer(self.openTime if isClose else self.closeTime, self.stop)
        self.stopTimer.start()

    def stop(self):
        self.setMoving(False)
        self.setLeft(False)

    def open(self):
        self.doAction(False)

    def close(self):
        self.doAction(True)

    def startOpen(self):
        self.stopTimer.cancel()
        self.setLeft(True)
        self.setMoving(True)

    def startClose(self):
        self.stopTimer.cancel()
        self.setLeft(False)
        self.setMoving(True)

    def setLight(self, state):
        self.light.setOnState(state)

    def getData(self):
        j = {
            "isMoving": self.isMovingPin.value,
            "isLeft": self.isLeftPin.value,
            "isLight": self.light.getLightValue(),
            "isNight": self.light.getIsNight(),
            "lightCount": self.light.getLightCount(),
            "lightOn": self.light.getOn(),
            "morning": self.light.morning.strftime("%H:%M:%S"),
            "evening": self.light.evening.strftime("%H:%M:%S"),
            "time": self.light.getTime()
        }
        return json.dumps(j)

    def getValues(self):
        status = "is moving: " + str(self.isMovingPin.value) + ", is left: " + str(self.isLeftPin.value) + ", is light: " + str(self.light.getLightValue())
        print(status)
        return status

    def setMoveTime(self, openTime, closeTime):
        try:
            self.openTime = int(openTime)
            self.closeTime = int(closeTime)
        except:
            print("Incorrect value to the move time")

    def getMoveTime(self):
        return self.openTime, self.closeTime

    def getTimes(self):
        return self.light.getTimes()

    def setTimes(self, morning, evening):
        self.light.setTimes(morning, evening)