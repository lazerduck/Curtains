from CurtainState import CurtainState
import json

class GetController:
    def __init__(self, state: CurtainState):
        self.state = state
        self.actions = {
            "open": self.open,
            "close": self.close,
            "stop": self.stop,
            "gettimes": self.getTimes,
            "getlimits": self.getLimits,
            "position": self.position,
            "targetposition": self.targetPosition,
            "state": self.state
        }
    
    def state(self):
        return json.dumps({
            "state": self.state
        })

    def open(self):
        self.state.setOpen()
        return "Opening"
    
    def close(self):
        self.state.setClosed()
        return "Closing"
    
    def position(self):
        return json.dumps({
            "position": self.state.position
        })
    
    def targetPosition(self):
        return json.dumps({
            "targetPosition": self.state.targetPosition
        })
    
    def stop(self):
        self.state.setTargetPosition(self.state.position)
        return "Stopped"
    
    def getTimes(self):
        return json.dumps({
            "allowOpeningFrom": self.state.allowOpeningFrom.isoformat(),
            "mustOpenBy": self.state.mustOpenBy.isoformat(),
            "allowClosingFrom": self.state.allowClosingFrom.isoformat(),
            "mustCloseBy": self.state.mustCloseBy.isoformat()
        })
    
    def getLimits(self):
        return json.dumps({
            "openLimit": self.state.openLimit,
            "closeLimit": self.state.closeLimit,
            "isCalibrated": self.state.isCalibrated
        })