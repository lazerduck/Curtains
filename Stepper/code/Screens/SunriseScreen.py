from .ScreenBase import ScreenBase
import CurtainState

class SunriseScreen(ScreenBase):
    def __init__(self, back) -> None:
        self.state = CurtainState.CurtainState()
        self.lines = ["Sunrise", "Sunset" "use sunrise", "back", "test"]
        self.selectedLine = 3
        self.back = back
        self.updateText()
        pass

    def rotaryButtonEvent(self):
        if(self.selectedLine == 2):
            self.state.useSunrise = not self.state.useSunrise
            self.state.saveState()
            self.back()
        
        if(self.selectedLine == 3):
            self.back()

    def rotaryAnticlockwiseEvent(self):
        self.selectedLine = self.selectedLine + 1
        if self.selectedLine > 3:
            self.selectedLine = 2
        self.updateText()

    
    def rotaryClockwiseEvent(self):
        self.selectedLine = self.selectedLine - 1
        if self.selectedLine < 2:
            self.selectedLine = 3
        self.updateText()

    def updateText(self):
        self.lines[0] = "Sunrise: " + self.state.SunriseData["results"]["sunrise"]
        self.lines[1] = "Sunset: " + self.state.SunriseData["results"]["sunset"]
        self.lines[2] = "use sunrise: " + str(self.state.useSunrise)
        self.lines[3] = "back"