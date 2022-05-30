import RPi.GPIO as GPIO
import logging
from systemd.journal import JournaldLogHandler

logger = logging.getLogger(__name__)
journald_handler = JournaldLogHandler()
logger.addHandler(journald_handler)

def placeHolder(obj):
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
        GPIO.add_event_detect(self.buttonOnePin, GPIO.RISING, callback=self.buttonOneCallback, bouncetime=300) 
        GPIO.add_event_detect(self.buttonTwoPin, GPIO.RISING, callback=self.buttonTwoCallback, bouncetime=300) 

    def buttonOneCallback(self, channel):
        print("btn_1")
        logger.info("btn_1")
        # self.buttonOneEvent()

    def buttonTwoCallback(self, channel):
        print("btn_2")
        logger.info("btn_2")
        # self.buttonTwoEvent()

    ## buttons seem to be being triggered when the motor changes?
    