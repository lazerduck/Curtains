from .Timings import Timing
from .ScreenBase import ScreenBase
from .ManualControlScreen import ManualControlScreen
from .Calibration import Calibration
from .ControlScreen import ControlScreen

class MainScreen(ScreenBase):
    def __init__(self, setScreen):
        self.lines = ["Main", "Calibrate", "Manual", "Contorl", "Times"]
        self.selectedLine = 2
        self.setScreen = setScreen

    def back(self):
        self.setScreen(self)

    def rotaryButtonEvent(self):
        print("rotaryButtonEvent")
        if self.selectedLine == 2:
            self.setScreen(Calibration(self.back))
            pass
        if self.selectedLine == 3:
            self.setScreen(ManualControlScreen(self.setScreen, self.back))
        if self.selectedLine == 4:
            self.setScreen(ControlScreen(self.setScreen, self.back))
        if self.selectedLine == 5:
            self.setScreen(Timing(self.back))
        pass
    
    def rotaryAnticlockwiseEvent(self):
        self.selectedLine = self.selectedLine + 1
        if self.selectedLine > 4:
            self.selectedLine = 2
    
    def rotaryClockwiseEvent(self):
        self.selectedLine = self.selectedLine - 1
        if self.selectedLine < 2:
            self.selectedLine = 4