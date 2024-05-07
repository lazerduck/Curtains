from CurtainState import CurtainState

class PostController:
    def __init__(self, state: CurtainState):
        self.state = state
        self.actions = {
            "goto": self.goTo,
            "settimes": self.setTimes,
            "setlimits": self.setLimits
        }

    def goTo(self, data):
        self.state.targetPosition = data["position"]
        return "Success"
    
    def setTimes(self, data):
        self.state.allowOpeningFrom = data["allowOpeningFrom"]
        self.state.mustOpenBy = data["mustOpenBy"]
        self.state.allowClosingFrom = data["allowClosingFrom"]
        self.state.mustCloseBy = data["mustCloseBy"]
        return "Success"
    
    def setLimits(self, data):
        self.state.openLimit = data["openLimit"]
        self.state.closeLimit = data["closeLimit"]
        self.state.isCalibrated = data["isCalibrated"]
        return "Success"

