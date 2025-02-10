from CurtainState import CurtainState
from SunRiseManager import SunRiseManager

class AutomationManager:
    def __init__(self, state:CurtainState, sunriseManager:SunRiseManager) -> None:
        self.state = state
        self.sunriseManager = sunriseManager
        pass

    def update(self):
        if not self.sunriseManager.isDataUpToDate():
            self.sunriseManager.initialiseSunRiseData()
        if self.state.isCalibrated:
            if self.state.useSunrise:
                if self.state.isNight and self.sunriseManager.isAfterSunrise():
                    self.state.setTargetPosition(self.state.openLimit)
                    self.state.setNight(False)
                    print("Opening")
                elif not self.state.isNight and self.sunriseManager.isAfterSunset():
                    self.state.setTargetPosition(self.state.closeLimit)
                    self.state.setNight(True)
                    print("Closing")
            else:
                if self.state.isNight and self.state.mustOpen():
                    self.state.setTargetPosition(self.state.openLimit)
                    self.state.setNight(False)
                    print("Opening")
                elif not self.state.isNight and self.state.mustClose():
                    self.state.setTargetPosition(self.state.closeLimit)
                    self.state.setNight(True)
                    print("Closing")