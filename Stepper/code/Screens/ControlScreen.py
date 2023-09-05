from .ScreenBase import ScreenBase
from CurtainState import CurtainState

class ControlScreen(ScreenBase):
    def __init__(self, setScreen, back) -> None:
        self.lines = ["Control", "Open", "Close", "Back"]
        self.selectedLine = 2
        self.isActivated = False
        self.state = CurtainState()
        self.setScreen = setScreen
        self.back = back

    def rotaryButtonEvent(self):
        if(self.selectedLine == 2):
            self.state.targetPosition = self.state.openLimit
        elif(self.selectedLine == 3):
            self.state.targetPosition = self.state.closeLimit
        elif(self.selectedLine == 4):
            self.back()

    def rotaryAnticlockwiseEvent(self):
        if(not self.isActivated):
            self.selectedLine = self.selectedLine + 1
            if self.selectedLine > 4:
                self.selectedLine = 2

    
    def rotaryClockwiseEvent(self):
        if(not self.isActivated):
            self.selectedLine = self.selectedLine - 1
            if self.selectedLine < 2:
                self.selectedLine = 4
