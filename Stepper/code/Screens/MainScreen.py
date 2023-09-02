from .ScreenBase import ScreenBase
from .ManualControlScreen import ManualControlScreen

class MainScreen(ScreenBase):
    def __init__(self, setScreen):
        self.lines = ["Main", "Calibrate", "Manual", ""]
        self.selectedLine = 2
        self.setScreen = setScreen

        def back():
            self.setScreen(self)

    def rotaryButtonEvent(self):
        print("rotaryButtonEvent")
        if self.selectedLine == 2:
            # change to the calibration screen
            pass
        if self.selectedLine == 3:
            self.setScreen(ManualControlScreen(self.setScreen, lambda: self.back()))
            # change to the manual control screen
        pass
    
    def rotaryAnticlockwiseEvent(self):
        self.selectedLine = self.selectedLine + 1
        if self.selectedLine > 4:
            self.selectedLine = 2
    
    def rotaryClockwiseEvent(self):
        self.selectedLine = self.selectedLine - 1
        if self.selectedLine < 2:
            self.selectedLine = 4