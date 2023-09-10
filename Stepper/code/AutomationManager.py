from CurtainState import CurtainState

class AutomationManager:
    def __init__(self, state:CurtainState) -> None:
        self.state = state
        pass

    def update(self):
        if self.state.isCalibrated:
            if self.state.isNight and self.state.mustOpen():
                self.state.setTargetPosition(self.state.openLimit)
                self.state.setNight(False)
            elif not self.state.isNight and self.state.mustClose():
                self.state.setTargetPosition(self.state.closeLimit)
                self.state.setNight(True)