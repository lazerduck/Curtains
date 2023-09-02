from .ScreenBase import ScreenBase

class MainScreen(ScreenBase):
    def __init__(self):
        self.lines = ["Main", "Calibrate", "", ""]
        self.selectedLine = 2

    def rightButtonEvent(self):
        if self.selectedLine == 2:
            # change to the calibration screen
            pass
        pass
    
    def rotaryAnticlockwiseEvent(self):
        print("rotaryClockwiseEvent")
        self.selectedLine = self.selectedLine + 1
        if self.selectedLine > 4:
            self.selectedLine = 2
    
    def rotaryClockwiseEvent(self):
        self.selectedLine = self.selectedLine - 1
        if self.selectedLine < 2:
            self.selectedLine = 4