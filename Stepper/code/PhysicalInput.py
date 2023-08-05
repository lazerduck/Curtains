from RotaryDriver.RotaryDriver import RotaryDriver
from RPi import GPIO

class PhysicalInput:
    def __init__(self, rotartyA, rotartyB, rotaryButton, buttonL, buttonR) -> None:
        self.rotaryDriver = RotaryDriver(rotartyA, rotartyB, rotaryButton)
        self.buttonL = buttonL
        self.buttonR = buttonR

        self.leftButtonEvent = self.defaultEvent
        self.rightButtonEvent = self.defaultEvent

        GPIO.setup(buttonL, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(buttonR, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

        GPIO.add_event_detect(buttonL, GPIO.RISING, 
            callback=self.leftButtonEvent)
        GPIO.add_event_detect(buttonR, GPIO.RISING, 
            callback=self.rightButtonEvent)

    def defaultEvent(self, e):
        pass

    def setLeftButtonEvent(self, event):
        self.leftButtonEvent = event

    def setRightButtonEvent(self, event):
        self.rightButtonEvent = event

    def setRotaryButtonEvent(self, event):
        self.rotaryDriver.buttonEvent = event

    def getRotaryPos(self):
        return self.rotaryDriver.pos
    
    def resetRotaryPos(self):
        self.rotaryDriver.resetPos()

