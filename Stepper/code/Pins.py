from RPi import GPIO

class pinData:
    def __init__(self, board, bcm) -> None:
        self.board = board
        self.bcm = bcm

    def get(self):
        if GPIO.getmode() == GPIO.BOARD:
            return self.board
        elif GPIO.getmode() == GPIO.BCM:
            return self.bcm
        else:
            raise Exception("GPIO mode not set")        
        
class Pins:
    def __init__(self) -> None:
        self.screenSCL = pinData(5, 3)
        self.screenSDA = pinData(3, 2)
        self.light = pinData(7, 4)
        self.step = pinData(24, 8)
        self.dir = pinData(26, 7)
        self.enable = pinData(8, 14)
        self.m0 = pinData(10, 15)
        self.m1 = pinData(12, 18)
        self.m2 = pinData(16, 23)
        self.sleep = pinData(18, 24)
        self.reset = pinData(22, 25)
        self.rotaryA = pinData(19, 10)
        self.rotaryB = pinData(21, 9)
        self.rotaryButton = pinData(36, 16)
        self.btnL = pinData(38, 20)
        self.btnR = pinData(40, 21)
