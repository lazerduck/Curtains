from SunRiseManager import SunRiseManager
import CurtainState

state = CurtainState.CurtainState()
sunriseManager = SunRiseManager(state)

sunriseManager.initialiseSunRiseData()
print(sunriseManager.isAfterSunrise())
print(sunriseManager.isAfterSunset())
print(sunriseManager.isDataUpToDate())