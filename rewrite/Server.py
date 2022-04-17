from http.server import HTTPServer, BaseHTTPRequestHandler
from Curtains import Curtains
from LightSensor import LightSensor
import json

class webHandler(BaseHTTPRequestHandler):
    controller = Curtains()
    sensor = LightSensor(controller)

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

    def do_GET(self):
        self.send_response(200)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()

        actions = {
            "open": self.open,
            "close": self.close,
            "stop": self.stop,
            "state": self.state
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
            "setlighttimes": self.setLightTime
        }

        pathVals = list(filter(None, self.path.split('/')))
        data = actions[pathVals[0].lower()](data)
        
        return



server = HTTPServer(('192.168.2.153',8080), webHandler)
server.serve_forever()