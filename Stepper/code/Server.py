from CurtainState import CurtainState
from http.server import HTTPServer, BaseHTTPRequestHandler
import datetime
import json

state = CurtainState()

class webHandler(BaseHTTPRequestHandler):

    def open(self):
        state.setOpen()
        return "Opening"

    def close(self):
        state.setClosed()
        return "Closing"

    def stop(self):
        state.setTargetPosition(state.position)
        return "Stopping"

    def state(self):
        data = {
            "position": state.position,
            "targetPosition": state.targetPosition,
            "speed": state.speed,
            "startSpeed": state.startSpeed,
            "stepMultiplier": state.stepMultiplier,
            "allowOpeningFrom": state.allowOpeningFrom.isoformat(),
            "mustOpenBy": state.mustOpenBy.isoformat(),
            "allowClosingFrom": state.allowClosingFrom.isoformat(),
            "mustCloseBy": state.mustCloseBy.isoformat(),
            "isNight": state.isNight,
            "openLimit": state.openLimit,
            "closeLimit": state.closeLimit,
            "isLightSensorEnabled": state.isLightSensorEnabled,
            "isCalibrated": state.isCalibrated
        }

        return json.dumps(data)
    
    def goTo(self, position):
        state.setTargetPosition(position)
    
    def do_GET(self):
        self.send_response(200)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()

        actions = {
            "open": self.open,
            "close": self.close,
            "stop": self.stop,
            "state": self.state,
        }

        pathVals = list(filter(None, self.path.split("/")))
        print(pathVals)
        if(actions.get(pathVals[0].lower()) == None):
            self.wfile.write(bytes("Invalid action", "utf-8"))
            return
        data = actions[pathVals[0].lower()]()
        if isinstance(data, str):
            self.wfile.write(bytes(data, "utf-8"))

    def do_POST(self):
        self.data_string = self.rfile.read(int(self.headers['Content-Length']))

        self.send_response(200)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()

        data = json.loads(self.data_string.decode("utf-8"))

        actions = {
            "goto": self.goTo,
        }

        pathVals = list(filter(None, self.path.split('/')))
        data = actions[pathVals[0].lower()](data)
        
        return