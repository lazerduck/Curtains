from datetime import timedelta
import datetime
from .ScreenBase import ScreenBase
import CurtainState

class Timing(ScreenBase):
    def __init__(self, back) -> None:
        self.state = CurtainState.CurtainState()
        self.lines = ["Timing", "Day", "Night", "back"]
        self.selectedLine = 2
        self.back = back
        self.isSettingDay = False
        self.isSettingNight = False
        self.updateText()

    def rotaryButtonEvent(self):
        if(self.selectedLine == 2):
            self.isSettingDay = not self.isSettingDay
            self.updateText()
        if(self.selectedLine == 3):
            self.isSettingNight = not self.isSettingNight
            self.updateText()
        if(self.selectedLine == 4):
            self.state.saveState()
            self.back()

    def rotaryAnticlockwiseEvent(self):
        if(self.isSettingDay):
            self.state.mustOpenBy = self.modifyTime(self.state.mustOpenBy, -1)
            self.updateText()
        elif(self.isSettingNight):
            self.state.mustCloseBy = self.modifyTime(self.state.mustCloseBy, -1)
            self.updateText()
        else:
            self.selectedLine = self.selectedLine + 1
            if self.selectedLine > 4:
                self.selectedLine = 2
    
    def rotaryClockwiseEvent(self):
        if(self.isSettingDay):
            self.state.mustOpenBy = self.modifyTime(self.state.mustOpenBy, 1)
            self.updateText()
        elif(self.isSettingNight):
            self.state.mustCloseBy = self.modifyTime(self.state.mustCloseBy, 1)
            self.updateText()
        else:
            self.selectedLine = self.selectedLine - 1
            if self.selectedLine < 2:
                self.selectedLine = 4

    def updateText(self):
        if(self.isSettingDay):
            self.lines[1] = " - Day: " + str(self.state.mustOpenBy)
        else:
            self.lines[1] = "Day: " + str(self.state.mustOpenBy)
        if(self.isSettingNight):
            self.lines[2] = " - Night: " + str(self.state.mustCloseBy)
        else:
            self.lines[2] = "Night: " + str(self.state.mustCloseBy)

    def modifyTime(self, time, minutes):
        dt = datetime.datetime.combine(datetime.datetime.today(), time) + timedelta(minutes=minutes)
        return dt.time()