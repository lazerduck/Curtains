import RPi.GPIO as GPIO
import threading
from datetime import time
import datetime

class LightContorl:
    lightPin = 13
    lightTime = 30
    lightCount = 0
    lightMax = 3
    isNight = True
    isOn = True
    isUsingTime = True
    morning = time(6,0,0,0)
    evening = time(15,0,0)

    def __init__(self, callBack):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.lightPin, GPIO.IN)
        self.callBack = callBack
        self.checkLight()
        
    def getLightValue(self):
        return not GPIO.input(self.lightPin)

    def getIsNight(self):
        return self.isNight

    def getLightCount(self):
        return self.lightCount

    def setOnState(self, state):
        self.isOn = state

    def getOn(self):
        return self.isOn

    def getTime(self):
        if(self.morning > datetime.datetime.now().time()):
            return "before morning"
        if(datetime.datetime.now().time() > self.evening):
            return "after evening"
        if(self.morning < datetime.datetime.now().time() and datetime.datetime.now().time() < self.evening):
            return "day time"
        else:
            return "unknown"

    def checkLight(self):
        threading.Timer(self.lightTime, self.checkLight).start()
        isBright = self.getLightValue()
        print("checking light, is bright: " + str(isBright) + " and is night: " + str(self.isNight) + " and count is: " + str(self.lightCount))

        if isBright == self.isNight:
            self.lightCount += 1

        if self.isOn:
            if self.lightCount >= self.lightMax:
                if(self.isUsingTime):
                    print(str(datetime.datetime.now().time()) + " " + str(self.morning) + ": " + str(self.morning < datetime.datetime.now().time() and self.isNight))
                    if (self.morning < datetime.datetime.now().time() and self.isNight) or (datetime.datetime.now().time() > self.evening and not self.isNight):
                        self.isNight = not self.isNight
                        self.callBack(not self.isNight)
                        self.lightCount = 0
                else:
                    self.isNight = not self.isNight
                    self.callBack(not self.isNight)
                    self.lightCount = 0
        else:
            self.lightCount = 0

    def getTimes(self):
        return self.morning, self.evening

    def setTimes(self, morning, evening):
        self.morning = datetime.datetime.strptime(morning, '%H:%M').time()
        self.evening = datetime.datetime.strptime(evening, '%H:%M').time()