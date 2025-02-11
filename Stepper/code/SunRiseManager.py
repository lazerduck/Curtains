from CurtainState import CurtainState
import requests
import time
from datetime import datetime

class SunRiseManager:
    def __init__(self, state: CurtainState) -> None:
        self.state = state

    def initialiseSunRiseData(self):
        response = requests.get("https://api.sunrisesunset.io/json?lat=53.766869&lng=-1.370976")
        data = response.json()
        self.state.SunriseData = data
        pass

    def isAfterSunrise(self):
        # convert the API time to a time object and compare it to the current time
        return datetime.now().time() > datetime.strptime(self.state.SunriseData["results"]["sunrise"], "%I:%M:%S %p").time()
    
    def isAfterSunset(self):
        # convert the API time to a time object and compare it to the current time
        return datetime.now().time() > datetime.strptime(self.state.SunriseData["results"]["sunset"], "%I:%M:%S %p").time()
    
    def isDataUpToDate(self):
        # check if the data is older than 24 hours
        return self.state.SunriseData["results"]["date"] == time.strftime("%Y-%m-%d")