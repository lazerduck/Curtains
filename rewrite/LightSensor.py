import RPi.GPIO as GPIO
from Curtains import Curtains
import threading
from datetime import date, time
import datetime

class LightSensor:
    controller: Curtains
    lightPin = 27
    lightTime = 30
    lightCount = 0
    lightMax = 3
    isNight = True
    isOn = True
    morning = time(6,0,0,0)
    evening = time(15,0,0)

    def __init__(self, curtains):
        self.controller = curtains
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.lightPin, GPIO.IN)
        self.isNight = not self.getLightValue()
        self.checkLight()

    def getLightValue(self):
        return not GPIO.input(self.lightPin)

    def isOutsideOfLimits(self):
        if(self.isNight):
            if(datetime.datetime.now().time() > self.morning):
                return True
        else:
            if(datetime.datetime.now().time() > self.evening):
                return True
        return False

    def checkLight(self):
        threading.Timer(self.lightTime, self.checkLight).start()
        if(not self.isOn):
            print("Skipping as turned off")
            return
        if not self.isOutsideOfLimits():
            print("Skipping as out of limits")
            return
        isLight = self.getLightValue()
        print("Sensor reports: " + str(isLight))
        if(self.isNight == isLight):
            self.lightCount += 1
        else:
            self.lightCount = 0
        
        print("Light count: " + str(self.lightCount))
        if(self.lightCount >= 3):
            if(self.isNight):
                self.controller.open()
            else:
                self.controller.close()
            self.isNight = not self.isNight