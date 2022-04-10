import RPi.GPIO as GPIO
import threading

class ButtonControl:
    openPin = 21
    closePin = 23
    pollRate = 0.1
    isActing = False

    def __init__(self, openCB, closeCB, stopCB):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.openPin, GPIO.IN)
        GPIO.setup(self.closePin, GPIO.IN)
        self.openCB = openCB
        self.closeCB = closeCB
        self.stopCB = stopCB
        print("Starting button loop")
        self.loop()

    def loop(self):
        threading.Timer(self.pollRate, self.loop).start()
        openPressed = not GPIO.input(self.openPin)
        closedPressed = not GPIO.input(self.closePin)
        print("openbtn = " + str(openPressed))
        print("is action = " + str(self.isActing))
        print("closebtn = " + str(closedPressed))
        if(openPressed):
            if(not self.isActing):
                self.openCB()
                print("btn open")
                self.isActing = True
        elif(closedPressed):
            if(not self.isActing):
                self.closeCB()
                print("btn close")
                self.isActing = True
        else:
            if(self.isActing):
                self.stopCB()
                self.isActing = False
                print("stop")
