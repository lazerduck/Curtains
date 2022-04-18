from time import sleep
import RPi.GPIO as GPIO

def placeHolder():
    print("Placeholder event")

class ButtonInput:
    buttonOnePin = 9
    buttonTwoPin = 11
    buttonOneEvent = placeHolder
    buttonTwoEvent = placeHolder

    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.buttonOnePin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(self.buttonTwoPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.add_event_detect(self.buttonOnePin, GPIO.RISING, callback=self.buttonOneEvent, bouncetime=300) 
        GPIO.add_event_detect(self.buttonTwoPin, GPIO.RISING, callback=self.buttonTwoEvent, bouncetime=300) 

    def buttonOneEvent(self, channel):
        print("btn_1")
        self.buttonOneEvent()

    def buttonTwoEvent(self, channel):
        print("btn_2")
        self.buttonTwoEvent()

obj = ButtonInput()

while(True):
    sleep(1)
    