from numpy import array
from Curtains import Curtains
from LightSensor import LightSensor
from Screen import Screen
import threading
from ButtonInput import ButtonInput

class CurrentScreen:
    screenMethod: any
    selectableRange: array
    actions: array
    selectPosition: int

class Output:
    curtains: Curtains
    sensor: LightSensor
    screen: Screen
    pollRate: 1
    oldData = ""
    ageCount = 0
    buttonInput: ButtonInput
    currentScreen: CurrentScreen

    def __init__(self, curtains, sensor):
        self.curtains = curtains
        self.sensor = sensor
        self.screen = Screen()
        self.buttonInput = ButtonInput()
        self.buttonInput.buttonOneEvent = self.move
        self.buttonInput.buttonTwoEvent = self.select
        self.currentScreen = CurrentScreen()
        self.timer = threading.Timer(0, self.curtains.stop)
        self.startMainMenuScreen()
        self.update()

    def update(self):
        threading.Timer(1, self.update).start()
        self.screen.active = self.ageCount < 60

        if(self.screen.active):
            self.screen.selectedLine = self.currentScreen.selectableRange[self.currentScreen.selectPosition]
            self.currentScreen.screenMethod()
        

        newData = str(self.curtains.state.move.Value)+ str(self.curtains.state.open.Value)+ str(self.sensor.getLightValue())
        if(self.oldData == newData):
            self.ageCount += 1
        else:
            self.ageCount = 0

        self.oldData = newData

    def select(self):
        self.ageCount = 0
        print("select")
        self.currentScreen.actions[self.currentScreen.selectPosition]()

    def move(self):
        self.ageCount = 0
        self.currentScreen.selectPosition += 1
        if(self.currentScreen.selectPosition >= len(self.currentScreen.selectableRange)):
            self.currentScreen.selectPosition = 0
        print("move")

    def statusScreen(self):
        self.screen.line1 = "< Status"
        self.screen.line2 = "Moving: " + str(self.curtains.state.move.Value)
        self.screen.line3 = "Is Night: " + str(self.sensor.isNight)
        self.screen.line4 = "Is Light: " + str(self.sensor.getLightValue())

    def mainMenu(self):
        self.screen.line1 = "Main Menu"
        self.screen.line2 = "Status"
        self.screen.line3 = "Manual Control"
        self.screen.line4 = ""

    def manualControl(self):
        self.screen.line1 = "< Manual Control"
        self.screen.line2 = "Open (1s)"
        self.screen.line3 = "Close (1s) "
        self.screen.line4 = ""

    def startStatusScreen(self):
        self.currentScreen.screenMethod = self.statusScreen
        self.currentScreen.selectableRange = [1]
        self.currentScreen.actions = [self.startMainMenuScreen]
        self.currentScreen.selectPosition = 0

    def startMainMenuScreen(self):
        self.currentScreen.screenMethod = self.mainMenu
        self.currentScreen.selectableRange = [2,3]
        self.currentScreen.actions = [self.startStatusScreen, self.startManualControlScreen]
        self.currentScreen.selectPosition = 0

    def startManualControlScreen(self):
        self.currentScreen.screenMethod = self.manualControl
        self.currentScreen.selectableRange = [1,2,3]
        self.currentScreen.actions = [self.startMainMenuScreen,self.openOneSecond, self.closeOneSecond]
        self.currentScreen.selectPosition = 0

    def openOneSecond(self):
        self.curtains.open()
        self.timer.cancel()
        self.timer = threading.Timer(1, self.curtains.stop)
        self.timer.start()

    def closeOneSecond(self):
        self.curtains.close()
        self.timer.cancel()
        self.timer = threading.Timer(1, self.curtains.stop)
        self.timer.start()

    