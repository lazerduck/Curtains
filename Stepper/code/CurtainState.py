from datetime import time, datetime
class CurtainState:
    def __init__(self) -> None:
        self.position = 0
        self.targetPosition = 0
        self.speed = 0.001
        self.allowOpeningFrom = time(6,0,0)
        self.mustOpenBy = time(10,0,0)
        self.allowClosingFrom = time(15,0,0)
        self.mustCloseBy = time(21,0,0)
        self.isNight = True
        self.openLimit = -10000
        self.closeLimit = 10000
        self.isLightSensorEnabled = True
        self.isCalibrated = True

    def defaultEvent(self):
        pass

    def setOpen(self):
        self.position = self.openLimit

    def setClosed(self):
        self.position = self.closeLimit

    def canOpen(self):
        return self.position > self.openLimit and self.isCalibrated
    
    def canClose(self):
        return self.position < self.closeLimit and self.isCalibrated
    
    def shouldOpenIfLight(self):
        return not self.isNight and self.canOpen() and datetime.now().time() > self.allowOpeningFrom

    def mustOpen(self):
        return self.canOpen() and datetime.now().time() > self.mustOpenBy
    
    def shouldCloseIfNight(self):
        return self.isNight and self.canClose() and datetime.now().time() > self.allowClosingFrom
    
    def mustClose(self):
        return self.canClose() and datetime.now().time() > self.mustCloseBy
    
    def setTargetPosition(self, targetPosition):
        if targetPosition < self.openLimit:
            targetPosition = self.openLimit
        if targetPosition > self.closeLimit:
            targetPosition = self.closeLimit
        self.targetPosition = targetPosition

    def setNight(self, isNight):
        self.isNight = isNight

    def setSpeed(self, speed):
        self.speed = speed
