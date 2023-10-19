from .Timings import Timing
from .ScreenBase import ScreenBase
from .ManualControlScreen import ManualControlScreen
from .Calibration import Calibration
from .ControlScreen import ControlScreen

class MainScreen(ScreenBase):
    def __init__(self, setScreen):
        self.fullLines = ["Main", "Calibrate", "Manual", "Contorl", "Times"]
        self.lines = ["Main", "Calibrate", "Manual", "Contorl"]
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
        if self.selectedLine > 5:
            self.selectedLine = 2
        self.updateLines()
    
    def rotaryClockwiseEvent(self):
        self.selectedLine = self.selectedLine - 1
        if self.selectedLine < 2:
            self.selectedLine = 5
        self.updateLines()

    def updateLines(self):
        length = len(self.fullLines)
        start = self.selectedLine - 2
        end = self.selectedLine + 2
        if start < 0:
            start = 0
            end = 4
        elif end > length:
            end = length
            start = length - 4
        self.lines = self.fullLines[start:end]