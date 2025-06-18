from http.server import BaseHTTPRequestHandler
from mutagen.mp3 import MP3
from io import BytesIO
import json

def handler(request):
    if request.method == "POST":
        try:
            # Get the file from the request
            file = request.files.get('file')
            if not file:
                return {
                    "statusCode": 400,
                    "body": json.dumps({"error": "No file uploaded"})
                }

            # Read the file content
            file_content = file.read()
            
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
