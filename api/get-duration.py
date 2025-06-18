from http.server import BaseHTTPRequestHandler
from mutagen.mp3 import MP3
from io import BytesIO
import json

class handler(BaseHTTPRequestHandler):
    def do_POST(self):
        try:
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            
            # Parse the multipart form data
            # This is a simplified version - you might need to adjust based on your needs
            file_data = post_data.split(b'\r\n\r\n')[1].split(b'\r\n--')[0]
            
            audio = MP3(BytesIO(file_data))
            duration = audio.info.length
            
            response = {
                "duration_seconds": round(duration, 2),
                "duration_formatted": f"{int(duration//60)}m {int(duration%60)}s"
            }
            
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(response).encode())
            
        except Exception as e:
            self.send_response(400)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({"error": str(e)}).encode())
    
    def do_GET(self):
        self.send_response(405)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps({"error": "Method Not Allowed"}).encode())
