from http.server import BaseHTTPRequestHandler
import json
import traceback
import base64
from mutagen.mp3 import MP3
import io

class handler(BaseHTTPRequestHandler):

    def do_POST(self):
        try:
            content_length = int(self.headers.get('Content-Length', 0))
            post_data = self.rfile.read(content_length)
            
            # Convert binary data to base64 string
            post_data_b64 = base64.b64encode(post_data).decode('ascii')

            # Calculate MP3 duration
            audio = MP3(io.BytesIO(post_data))
            duration_seconds = audio.info.length

            self.send_response(200)
            self.send_header('Content-type','application/json')
            self.end_headers()
            
            # Create a proper JSON response with duration
            response = {
                "value": post_data_b64,
                "duration_seconds": duration_seconds
            }
            message = json.dumps(response)
            self.wfile.write(message.encode())
            return
        except Exception as e:
            # Log the error
            print(f"Error processing request: {str(e)}")
            print(traceback.format_exc())
            
            # Send error response
            self.send_response(500)
            self.send_header('Content-type','application/json')
            self.end_headers()
            error_response = {"error": str(e)}
            self.wfile.write(json.dumps(error_response).encode())
            return

    def do_GET(self):
        self.send_response(400)
        self.send_header('Content-type','application/json')
        self.end_headers()
        message = '{"error": "POST REQUEST ONLY"}'
        self.wfile.write(message.encode())
        return