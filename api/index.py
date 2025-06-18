from http.server import BaseHTTPRequestHandler

class handler(BaseHTTPRequestHandler):

    def do_POST(self):
        content_length = int(self.headers.get('Content-Length', 0))
        post_data = self.rfile.read(content_length)
        

        self.send_response(200)
        self.send_header('Content-type','application/json')
        self.end_headers()
        message = '{"value": post_data}'
        self.wfile.write(message.encode())
        return

    def do_GET(self):
        self.send_response(400)
        self.send_header('Content-type','application/json')
        self.end_headers()
        message = '{"error": "POST REQUEST ONLY"}'
        self.wfile.write(message.encode())
        return