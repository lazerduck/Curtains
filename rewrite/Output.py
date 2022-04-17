from Curtains import Curtains
from LightSensor import LightSensor
from Screen import Screen
import threading

class Output:
    curtains: Curtains
    sensor: LightSensor
    screen: Screen
    pollRate: 5

    def __init__(self, curtains, sensor):
        self.curtains = curtains
        self.sensor = sensor
        self.screen = Screen()
        self.update()

    def update(self):
        threading.Timer(self.pollRate, self.update).start()
        self.screen.line1 = "Status"
        self.screen.line2 = "Moving: " + str(self.curtains.state.move.Value)
        self.screen.line3 = "Open: " + str(self.curtains.state.open.Value)
        self.screen.line4 = "Is Light: " + str(self.sensor.getLightValue())

    