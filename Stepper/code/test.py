from SunRiseManager import SunRiseManager
import CurtainState
import json

state = CurtainState.CurtainState()
sunriseManager = SunRiseManager(state)

sunriseManager.initialiseSunRiseData()
print(sunriseManager.isAfterSunrise())
print(sunriseManager.isAfterSunset())
print(sunriseManager.isDataUpToDate())

print( json.dumps({
            "position": state.position,
            "targetPosition": state.targetPosition,
            "speed": state.speed,
            "startSpeed": state.startSpeed,
            "stepMultiplier": state.stepMultiplier,
            "allowOpeningFrom": state.allowOpeningFrom.isoformat(),
            "mustOpenBy": state.mustOpenBy.isoformat(),
            "allowClosingFrom": state.allowClosingFrom.isoformat(),
            "mustCloseBy": state.mustCloseBy.isoformat(),
            "isNight": state.isNight,
            "openLimit": state.openLimit,
            "closeLimit": state.closeLimit,
            "isLightSensorEnabled": state.isLightSensorEnabled,
            "isCalibrated": state.isCalibrated,
            "useSunrise": state.useSunrise,
            "SunriseData": state.SunriseData
        }, indent=2))