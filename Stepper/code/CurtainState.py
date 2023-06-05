from datetime import time, datetime
class CurtainState:
    def __init__(self) -> None:
        self.position = 0
        self.targetPosition = 0
        self.speed = 0
        self.allowOpeningFrom = time(6,0,0)
        self.mustOpenBy = time(10,0,0)
        self.allowClosingFrom = time(15,0,0)
        self.mustCloseBy = time(21,0,0)
        self.isNight = True
        self.isEnabled = True

    def canOpen(self):
        return self.position == 0 and self.isEnabled # get these limits
    
    def canClose(self):
        return self.position == 100 and self.isEnabled # get these limits
    
    def shouldOpenIfLight(self):
        return not self.isNight and self.canOpen() and datetime.now().time() > self.allowOpeningFrom

    def mustOpenIfLight(self):
        return not self.isNight and self.canOpen() and datetime.now().time() > self.mustOpenBy
    
    def shouldCloseIfNight(self):
        return self.isNight and self.canClose() and datetime.now().time() > self.allowClosingFrom
    
    def mustCloseIfNight(self):
        return self.isNight and self.canClose() and datetime.now().time() > self.mustCloseBy
    
    def setTargetPosition(self, targetPosition):
        self.targetPosition = targetPosition

    def disable(self):
        self.isEnabled = False

    def enable(self):
        self.isEnabled = True

    def setNight(self, isNight):
        self.isNight = isNight

    def setSpeed(self, speed):
        self.speed = speed
