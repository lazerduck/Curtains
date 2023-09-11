from CurtainState import CurtainState
from http.server import HTTPServer, BaseHTTPRequestHandler
import datetime
import json

class webHandler(BaseHTTPRequestHandler):
    state = CurtainState()

    def open(self):
        self.state.setOpen()

    def close(self):
        self.state.setClosed()

    def stop(self):
        self.state.setTargetPosition(self.state.position)

    def state(self):
        data = {
            "position": self.state.position,
            "targetPosition": self.state.targetPosition,
            "speed": self.state.speed,
            "startSpeed": self.state.startSpeed,
            "stepMultiplier": self.state.stepMultiplier,
            "allowOpeningFrom": self.state.allowOpeningFrom.isoformat(),
            "mustOpenBy": self.state.mustOpenBy.isoformat(),
            "allowClosingFrom": self.state.allowClosingFrom.isoformat(),
            "mustCloseBy": self.state.mustCloseBy.isoformat(),
            "isNight": self.state.isNight,
            "openLimit": self.state.openLimit,
            "closeLimit": self.state.closeLimit,
            "isLightSensorEnabled": self.state.isLightSensorEnabled,
            "isCalibrated": self.state.isCalibrated
        }

        return json.dumps(data)
    
    def goTo(self, position):
        self.state.setTargetPosition(position)
    
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