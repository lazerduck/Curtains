from ScreenBase import ScreenBase
import CurtainState


class Calibration(ScreenBase):
    def __init__(self, back) -> None:
        self.state = CurtainState.CurtainState()
        self.lines = ["Calibration", "open", "close", "back"]
        self.selectedLine = 2
        self.back = back
        self.isSettingOpen = False
        self.isSettingClose = False
        self.isOpenSet = False
        self.isCloseSet = False
        pass

    def rotaryButtonEvent(self):
        if(self.selectedLine == 2):
            if(self.isSettingOpen):
                self.state.openLimit = self.state.position
                self.isOpenSet = True
            self.isSettingOpen = not self.isSettingOpen

        if(self.selectedLine == 3):
            if(self.isSettingClose):
                self.state.closeLimit = self.state.position
                self.isCloseSet = True
            self.isSettingClose = not self.isSettingClose

        if(self.isOpenSet and self.isCloseSet):
            self.state.isCalibrated = True
        
        if(self.selectedLine == 4):
            self.back()

    def rotaryAnticlockwiseEvent(self):
        if(not self.isSettingOpen or self.isSettingClose):
            self.selectedLine = self.selectedLine + 1
            if self.selectedLine > 4:
                self.selectedLine = 2
        else:
            self.state.setTargetPosition(self.state.position + (1 * self.state.stepMultiplier))

    
    def rotaryClockwiseEvent(self):
        if(not self.isSettingOpen or self.isSettingClose):
            self.selectedLine = self.selectedLine - 1
            if self.selectedLine < 2:
                self.selectedLine = 4
        else:
            self.state.setTargetPosition(self.state.position - (1 * self.state.stepMultiplier))

    def updateText(self):
        if(self.isSettingOpen):
            self.lines[1] = "open: " + str(self.state.position)
        
        if(self.isSettingClose):
            self.lines[2] = "close: " + str(self.state.position)