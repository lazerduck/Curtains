from Curtains import Curtains
from LightSensor import LightSensor
from Screen import Screen
import threading
from ButtonInput import ButtonInput

class Output:
    curtains: Curtains
    sensor: LightSensor
    screen: Screen
    pollRate: 1
    oldData = ""
    ageCount = 0
    buttonInput: ButtonInput

    def __init__(self, curtains, sensor):
        self.curtains = curtains
        self.sensor = sensor
        self.screen = Screen()
        self.buttonInput = ButtonInput()
        self.buttonInput.buttonOneEvent = self.activateScreen
        self.update()

    def update(self):
        threading.Timer(1, self.update).start()
        lightSensorValue = self.sensor.getLightValue()
        self.screen.active = self.ageCount < 60
        if(self.ageCount < 60):
            self.screen.line1 = "Status"
            self.screen.line2 = "Moving: " + str(self.curtains.state.move.Value)
            self.screen.line3 = "Is Night: " + str(self.sensor.isNight)
            self.screen.line4 = "Is Light: " + str()

        newData = str(self.curtains.state.move.Value)+ str(self.curtains.state.open.Value)+ str(self.sensor.getLightValue())
        if(self.oldData == newData):
            self.ageCount += 1
        else:
            self.ageCount = 0

        self.oldData = newData

    def activateScreen(self):
        self.ageCount = 0

    