class ScreenBase:
    def __init__(self) -> None:
        self.lines = ["", "", "", ""]
        self.selectedLine = 0
        pass
        
    def leftButtonEvent(self):
        pass

    def rightButtonEvent(self):
        pass

    def rotaryClockwiseEvent(self):
        pass

    def rotaryAnticlockwiseEvent(self):
        pass

    def rotaryButtonEvent(self):
        pass

    def getLines(self):
        return self.lines

    def getSelectedLine(self):
        0
