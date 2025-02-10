from .ScreenBase import ScreenBase
import CurtainState

class SunriseScreen(ScreenBase):
    def __init__(self, back) -> None:
        self.state = CurtainState.CurtainState()
        self.lines = ["Sunrise", "Sunset" "use sunrise", "back"]
        self.selectedLine = 3
        self.back = back
        self.updateText()
        pass

    def rotaryButtonEvent(self):
        if(self.selectedLine == 3):
            self.state.useSunrise = not self.state.useSunrise
            self.state.saveState()
            self.back()
        
        if(self.selectedLine == 4):
            self.back()

    def rotaryAnticlockwiseEvent(self):
        self.selectedLine = self.selectedLine + 1
        if self.selectedLine > 4:
            self.selectedLine = 3
        self.updateText()

    
    def rotaryClockwiseEvent(self):
        self.selectedLine = self.selectedLine - 1
        if self.selectedLine < 3:
            self.selectedLine = 4
        self.updateText()

    def updateText(self):
        self.lines[1] = "Sunrise: " + self.state.SunriseData["results"]["sunrise"]
        self.lines[2] = "Sunset: " + self.state.SunriseData["results"]["sunset"]
        self.lines[3] = "use sunrise: " + str(self.state.useSunrise)
        self.screen.setLines(self.lines, self.selectedLine)