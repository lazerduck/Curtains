from http.server import HTTPServer, BaseHTTPRequestHandler
from MotorControl import MotorControl
import json

class webHandler(BaseHTTPRequestHandler):
    motor = MotorControl()

    def left(self):
        self.motor.doAction(True)
        print("Turning left")
        return "Left"

    def right(self):
        self.motor.doAction(False)
        print("Turning right")
        return "Right"

    def stop(self):
        self.motor.stop()
        return "Stopping"
    
    def startOpen(self):
        self.motor.startOpen()

    def startClose(self):
        return self.motor.startClose()

    def getData(self):
        self.motor.getValues()

    def data(self):
        return self.motor.getData()

    def lightOn(self):
        self.motor.setLight(True)

    def lightOff(self):
        self.motor.setLight(False)

    def getTravelTime(self):
        print("Get time")
        open, close = self.motor.getMoveTime()
        return json.dumps({
            "open": open,
            "close": close
        })

    def getLightTime(self):
        print("Get light")
        morning, evening = self.motor.getTimes()
        return json.dumps({
            "morning": morning.strftime("%H:%M"),
            "evening": evening.strftime("%H:%M")
        })

    def setLightTime(self, data):
        self.motor.setTimes(data["morning"], data["evening"])

    def setMoveTimes(self, data):
        print(json.dumps(data))
        self.motor.setMoveTime(data["openTime"], data["closeTime"])

    def do_GET(self):
        self.send_response(200)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()

        actions = {
            "left": self.left,
            "open": self.left,
            "right": self.right,
            "close": self.right,
            "stop": self.stop,
            "data": self.data,
            "startopen": self.startOpen,
            "startclose": self.startClose,
            "getdata": self.getData,
            "lighton": self.lightOn,
            "lightoff": self.lightOff,
            "traveltimes": self.getTravelTime,
            "lighttimes": self.getLightTime
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