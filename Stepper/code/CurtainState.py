from datetime import time, datetime
import os.path
import atexit


def singleton(cls):
    instances = {}

    def getInstance():
        if cls not in instances:
            instances[cls] = cls()
        return instances[cls]

    return getInstance


@singleton
class CurtainState:
    def __init__(self) -> None:
        self.position = 0
        self.targetPosition = 0
        self.speed = 0.0001
        self.startSpeed = 0.01
        self.stepMultiplier = 200
        self.allowOpeningFrom = time(6, 0, 0)
        self.mustOpenBy = time(8, 0, 0)
        self.allowClosingFrom = time(15, 0, 0)
        self.mustCloseBy = time(21, 00, 0)
        self.isNight = False
        self.openLimit = 0
        self.closeLimit = 0
        self.isLightSensorEnabled = True
        self.isCalibrated = True
        self.useSunrise = True
        self.SunriseData = {
            "results": {
                "sunrise": "06:00:00",
                "sunset": "21:00:00",
                "date": "2021-01-01",
            }
        }
        self.loadStoredState()
        atexit.register(self.saveState)

    def loadStoredState(self):
        print(os.getcwd())
        if not os.path.isfile("state.txt"):
            return

        file = open("state.txt", "r")

        self.position = int(file.readline())
        self.targetPosition = self.position
        file.readline()
        self.speed = float(file.readline())
        self.startSpeed = float(file.readline())
        self.stepMultiplier = int(file.readline())
        self.allowOpeningFrom = time.fromisoformat(file.readline().replace("\n", ""))
        self.mustOpenBy = time.fromisoformat(file.readline().replace("\n", ""))
        self.allowClosingFrom = time.fromisoformat(file.readline().replace("\n", ""))
        self.mustCloseBy = time.fromisoformat(file.readline().replace("\n", ""))
        self.isNight = bool(file.readline())
        self.openLimit = int(file.readline())
        self.closeLimit = int(file.readline())
        self.isLightSensorEnabled = bool(file.readline())
        self.isCalibrated = bool(file.readline())

        file.close()

    def saveState(self):
        file = open("state.txt", "w")

        file.write(str(self.position) + "\n")
        file.write("0\n")
        file.write(str(self.speed) + "\n")
        file.write(str(self.startSpeed) + "\n")
        file.write(str(self.stepMultiplier) + "\n")
        file.write(self.allowOpeningFrom.isoformat() + "\n")
        file.write(self.mustOpenBy.isoformat() + "\n")
        file.write(self.allowClosingFrom.isoformat() + "\n")
        file.write(self.mustCloseBy.isoformat() + "\n")
        file.write(str(self.isNight) + "\n")
        file.write(str(self.openLimit) + "\n")
        file.write(str(self.closeLimit) + "\n")
        file.write(str(self.isLightSensorEnabled) + "\n")
        file.write(str(self.isCalibrated) + "\n")

        file.close()

    def defaultEvent(self):
        pass

    def setOpen(self):
        self.targetPosition = self.openLimit

    def setClosed(self):
        self.targetPosition = self.closeLimit

    def canOpen(self):
        return True  # self.position > self.openLimit and self.isCalibrated

    def canClose(self):
        return True  # self.position < self.closeLimit and self.isCalibrated

    def shouldOpenIfLight(self):
        return (
            not self.isNight
            and self.canOpen()
            and datetime.now().time() > self.allowOpeningFrom
        )

    def mustOpen(self):
        return (
            self.canOpen()
            and datetime.now().time() > self.mustOpenBy
            and datetime.now().time() < self.allowClosingFrom
        )

    def shouldCloseIfNight(self):
        return (
            self.isNight
            and self.canClose()
            and datetime.now().time() > self.allowClosingFrom
        )

    def mustClose(self):
        return self.canClose() and datetime.now().time() > self.mustCloseBy

    def setTargetPosition(self, targetPosition):
        if self.isCalibrated:
            if targetPosition < self.openLimit:
                targetPosition = self.openLimit
            if targetPosition > self.closeLimit:
                targetPosition = self.closeLimit
        self.targetPosition = targetPosition

    def setNight(self, isNight):
        self.isNight = isNight

    def setSpeed(self, speed):
        self.speed = speed
