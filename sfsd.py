from http.server import SimpleHTTPRequestHandler, HTTPServer

class RequestHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        print(f"Received request: {self.path}")
        self.send_response(200)
        self.end_headers()

server = HTTPServer(('0.0.0.0', 8000), RequestHandler)
print("Server started on port 8000")
server.serve_forever()