from CurtainState import CurtainState
import requests
import time

class SunRiseManager:
    def __init__(self, state: CurtainState) -> None:
        self.state = state

    def initialiseSunRiseData(self):
        response = requests.get("https://api.sunrisesunset.io/json?lat=53.766869&lng=-1.370976")
        data = response.json()
        self.state.SunriseData = data
        pass

    def isAfterSunrise(self):
        return self.state.SunriseData["results"]["sunrise"] < time.strftime("%H:%M:%S")
    
    def isAfterSunset(self):
        return self.state.SunriseData["results"]["sunset"] < time.strftime("%H:%M:%S")
    
    def isDataUpToDate(self):
        return self.state.SunriseData["date"] == time.strftime("%Y-%m-%d")