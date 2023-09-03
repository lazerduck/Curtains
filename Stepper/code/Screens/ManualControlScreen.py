from .ScreenBase import ScreenBase
from CurtainState import CurtainState

class ManualControlScreen(ScreenBase):
    def __init__(self, setScreen, back) -> None:
        self.lines = ["Manual Control", "Activate", "Back", "Pos"]
        self.selectedLine = 2
        self.isActivated = False
        self.curtainState = CurtainState()
        self.setScreen = setScreen
        self.back = back

    def rotaryButtonEvent(self):
        if(self.selectedLine == 2):
            self.isActivated = not self.isActivated
            self.lines[1] = "Deactivate" if self.isActivated else "Activate"
        elif(self.selectedLine == 3):
            self.back()

    def rotaryAnticlockwiseEvent(self):
        if(not self.isActivated):
            self.selectedLine = self.selectedLine + 1
            if self.selectedLine > 4:
                self.selectedLine = 2
        else:
            self.curtainState.setTargetPosition(self.curtainState.position + (1 * self.curtainState.stepMultiplier))
            self.lines[3] = "pos: " + str(self.curtainState.position)

    
    def rotaryClockwiseEvent(self):
        if(not self.isActivated):
            self.selectedLine = self.selectedLine - 1
            if self.selectedLine < 2:
                self.selectedLine = 4
        else:
            self.curtainState.setTargetPosition(self.curtainState.position - (1 * self.curtainState.stepMultiplier))
            self.lines[3] = "pos: " + str(self.curtainState.position)
