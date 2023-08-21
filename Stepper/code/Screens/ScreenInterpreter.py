from Screen import Screen
from PhysicalInput import PhysicalInput
from ScreenBase import ScreenBase

class ScreenInterpreter:
    def __init__(self, screen:Screen, physicalInput:PhysicalInput) -> None:
        self.screen = screen
        self.physicalInput = physicalInput
        self.currentScreen = ScreenBase()

    def setScreen(self, screen:ScreenBase):
        self.currentScreen = screen
        self.physicalInput.setLeftButtonEvent(screen.leftButtonEvent)
        self.physicalInput.setRightButtonEvent(screen.rightButtonEvent)
        self.physicalInput.setRotaryButtonEvent(screen.rotaryButtonEvent)
        self.physicalInput.setClockwiseEvent(screen.rotaryClockwiseEvent)
        self.physicalInput.setAntiClockwiseEvent(screen.rotaryAnticlockwiseEvent)

    def update(self):
        lines = self.currentScreen.getLines()
        self.screen.line1 = lines[0]
        self.screen.line2 = lines[1]
        self.screen.line3 = lines[2]
        self.screen.line4 = lines[3]
        self.screen.selectedLine = self.currentScreen.getSelectedLine()
        # no need to update the screen, seems it does that on its own
