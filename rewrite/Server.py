from http.server import HTTPServer, BaseHTTPRequestHandler
from Curtains import Curtains
from LightSensor import LightSensor
from Output import Output
import datetime
import json

class webHandler(BaseHTTPRequestHandler):
    controller = Curtains()
    sensor = LightSensor(controller)
    output = Output(controller, sensor)

    def open(self):
        self.controller.open()

    def close(self):
        self.controller.close()

    def stop(self):
        self.controller.stop()

    def state(self):
        data = {
            "isMoving": self.controller.state.move.Value,
            "isOpening": self.controller.state.open.Value,
            "openTime": self.controller.state.openTime,
            "closeTime": self.controller.state.closeTime,
            "lightCount": self.sensor.lightCount,
            "isBright": self.sensor.getLightValue(),
            "isLightSensorOn": self.sensor.isOn,
            "isNight": self.sensor.isNight,
            "morning": self.sensor.morning.strftime("%H:%M"),
            "evening": self.sensor.evening.strftime("%H:%M")
        }
        return json.dumps(data)

    def setLightTime(self, data):
        self.sensor.morning =  datetime.datetime.strptime(data["morning"], '%H:%M').time()
        self.sensor.evening = datetime.datetime.strptime(data["evening"], '%H:%M').time()

    def setMoveTimes(self, data):
        self.controller.openTime = int(data["openTime"])
        self.controller.closeTime = int(data["closeTime"])

    def do_GET(self):
        self.send_response(200)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()

        actions = {
            "open": self.open,
            "close": self.close,
            "stop": self.stop,
            "state": self.state,
            # legacy
            "startopen": self.open,
            "startclose": self.close,
            "left": self.open,
            "right": self.close
        }

        pathVals = list(filter(None, self.path.split('/')))
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
            "setlighttimes": self.setLightTime,
            "setmovetimes": self.setMoveTimes
        }

        pathVals = list(filter(None, self.path.split('/')))
        data = actions[pathVals[0].lower()](data)
        
        return



server = HTTPServer(('192.168.2.152',8080), webHandler)
server.serve_forever()