from .ScreenBase import ScreenBase
import CurtainState


class Calibration(ScreenBase):
    def __init__(self, back) -> None:
        self.state = CurtainState.CurtainState()
        self.lines = ["Calibration", "open", "close", "back"]
        self.selectedLine = 2
        self.back = back
        self.state.isCalibrated = False
        self.isSettingOpen = False
        self.isSettingClose = False
        self.isOpenSet = False
        self.isCloseSet = False
        self.updateText()
        pass

    def rotaryButtonEvent(self):
        if(self.selectedLine == 2):
            self.isSettingOpen = not self.isSettingOpen
            self.updateText()
            if(not self.isSettingOpen):
                self.state.openLimit = self.state.position
                self.isOpenSet = True

        if(self.selectedLine == 3):
            self.isSettingClose = not self.isSettingClose
            self.updateText()
            if(not self.isSettingClose):
                self.state.closeLimit = self.state.position
                self.isCloseSet = True
        
        if(self.selectedLine == 4):
            if(self.isOpenSet and self.isCloseSet):
                self.state.isCalibrated = True
            self.state.saveState()
            self.back()

    def rotaryAnticlockwiseEvent(self):
        if(not self.isSettingOpen and not self.isSettingClose):
            self.selectedLine = self.selectedLine + 1
            if self.selectedLine > 4:
                self.selectedLine = 2
        else:
            self.state.setTargetPosition(self.state.position + (1 * self.state.stepMultiplier))
            self.updateText()

    
    def rotaryClockwiseEvent(self):
        if(not self.isSettingOpen and not self.isSettingClose):
            self.selectedLine = self.selectedLine - 1
            if self.selectedLine < 2:
                self.selectedLine = 4
        else:
            self.state.setTargetPosition(self.state.position - (1 * self.state.stepMultiplier))
            self.updateText()

    def updateText(self):
        if(self.isSettingOpen):
            self.lines[1] = " - open: " + str(self.state.position)
        else:
            self.lines[1] = " open: " + str(self.state.openLimit)


        if(self.isSettingClose):
            self.lines[2] = " - close: " + str(self.state.position)
        else:
            self.lines[2] = " close: " + str(self.state.closeLimit)
