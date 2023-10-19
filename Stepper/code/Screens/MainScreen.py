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
        self.selectedOption = 2
        self.setScreen = setScreen

    def back(self):
        self.setScreen(self)

    def rotaryButtonEvent(self):
        print("rotaryButtonEvent")
        if self.selectedOption == 2:
            self.setScreen(Calibration(self.back))
            pass
        if self.selectedOption == 3:
            self.setScreen(ManualControlScreen(self.setScreen, self.back))
        if self.selectedOption == 4:
            self.setScreen(ControlScreen(self.setScreen, self.back))
        if self.selectedOption == 5:
            self.setScreen(Timing(self.back))
        pass
    
    def rotaryAnticlockwiseEvent(self):
        self.selectedOption = self.selectedOption + 1
        if self.selectedOption > 4:
            self.selectedOption = 2
        self.updateLines()
    
    def rotaryClockwiseEvent(self):
        self.selectedOption = self.selectedOption - 1
        if self.selectedOption < 2:
            self.selectedOption = 4
        self.updateLines()

    def updateLines(self):
        length = len(self.fullLines)
        start = self.selectedOption - 3
        end = self.selectedOption
        if start < 0:
            start = 0
            end = 4
        elif end > length:
            end = length
            start = length - 4
        self.lines = self.fullLines[start:end]

        option = self.fullLines[self.selectedOption]
        print(str(self.lines))
        print(str(self.selectedLine))
        print(str(self.selectedOption))
        print(option)
        self.selectedLine = self.lines.index(option) + 1
        