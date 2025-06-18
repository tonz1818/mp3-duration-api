from http.server import BaseHTTPRequestHandler
import json

class handler(BaseHTTPRequestHandler):

    def do_POST(self):
        content_length = int(self.headers.get('Content-Length', 0))
        post_data = self.rfile.read(content_length)
        
        # Decode the post data from bytes to string
        post_data_str = post_data.decode('utf-8')

        self.send_response(200)
        self.send_header('Content-type','application/json')
        self.end_headers()
        
        # Create a proper JSON response
        response = {"value": post_data_str}
        message = json.dumps(response)
        self.wfile.write(message.encode())
        return

    def do_GET(self):
        self.send_response(400)
        self.send_header('Content-type','application/json')
        self.end_headers()
        message = '{"error": "POST REQUEST ONLY"}'
        self.wfile.write(message.encode())
        return