from CurtainState import CurtainState
from http.server import HTTPServer, BaseHTTPRequestHandler
import json
from Controllers.Get import GetController
from Controllers.Post import PostController

state = CurtainState()
get = GetController(state)
post = PostController(state)

class webHandler(BaseHTTPRequestHandler):
    
    def do_GET(self):
        self.send_response(200)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()

        actions = get.actions

        pathVals = list(filter(None, self.path.split("/")))
        print(pathVals)
        print(actions)
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

        actions = post.actions

        pathVals = list(filter(None, self.path.split('/')))
        response = actions[pathVals[0].lower()](data)

        if isinstance(response, str):
            self.wfile.write(bytes(response, "utf-8"))
        
        return