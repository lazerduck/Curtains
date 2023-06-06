import RPi.GPIO as GPIO

class RotaryDriver:
    def __init__(self, rotaryPin1, rotaryPin2, buttonPin) -> None:
        self.rotaryPin1 = rotaryPin1
        self.rotaryPin2 = rotaryPin2
        self.buttonPin = buttonPin
        self.pos = 0
        self.state = 0
        self.buttonEvent = self.defaultEvent
        self.clockwiseEvent = self.defaultEvent
        self.anticlockwiseEvent = self.defaultEvent

        GPIO.setup(rotaryPin1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(rotaryPin2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

        GPIO.add_event_detect(rotaryPin1, GPIO.RISING, 
            callback=self.rp1Rising)

        GPIO.add_event_detect(rotaryPin2, GPIO.RISING, 
            callback=self.rp2Rising)
        
        GPIO.add_event_detect(buttonPin, GPIO.RISING, 
            callback=self.buttonRising)
        
    def defaultEvent(self):
        pass

    def buttonRising(self, e):
        self.buttonEvent()
        
    def rot(self):
        if self.state == 1:
            self.pos += 1 # Clockwise
            self.clockwiseEvent()
        if self.state == 2:
            self.pos -= 1 # Anti-clockwise
            self.anticlockwiseEvent()
        self.state = 0

    def rp1Rising(self, e):
        p1 = GPIO.input(self.rotaryPin1)
        p2 = GPIO.input(self.rotaryPin2)
        if p1 == 1 and p2 == 0:
            self.state =1
        if p1 == 1 and p2 == 1:
            self.rot()

    def rp2Rising(self, e):
        p1 = GPIO.input(self.rotaryPin1)
        p2 = GPIO.input(self.rotaryPin2)
        if p2 == 1 and p1 == 0:
            self.state = 2
        if p1 == 1 and p2 == 1:
            self.rot()

    def resetPos(self):
        self.pos = 0
