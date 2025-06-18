from http.server import BaseHTTPRequestHandler
from mutagen.mp3 import MP3
from io import BytesIO
import json

def handler(request):
    if request.method == "POST":
        try:
            # Get the raw body from the request
            content_length = int(request.headers.get('Content-Length', 0))
            if content_length == 0:
                return {
                    "statusCode": 400,
                    "body": json.dumps({"error": "No file uploaded"})
                }

            # Read the raw body
            file_content = request.body
            
            # Process the MP3 file
            audio = MP3(BytesIO(file_content))
            duration = audio.info.length
            
            return {
                "statusCode": 200,
                "headers": {"Content-Type": "application/json"},
                "body": json.dumps({
                    "duration_seconds": round(duration, 2),
                    "duration_formatted": f"{int(duration//60)}m {int(duration%60)}s"
                })
            }
            
        except Exception as e:
            return {
                "statusCode": 400,
                "body": json.dumps({"error": str(e)})
            }
    
    return {
        "statusCode": 405,
        "body": json.dumps({"error": "Method Not Allowed"})
    }
