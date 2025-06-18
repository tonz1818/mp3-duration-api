from mutagen.mp3 import MP3
from io import BytesIO

def handler(request):
    # Ensure a file was uploaded
    if request.method != "POST":
        return {
            "statusCode": 405,
            "body": "Method Not Allowed"
        }

    if not request.files or "file" not in request.files:
        return {
            "statusCode": 400,
            "body": "No file uploaded"
        }

    file = request.files["file"]
    audio = MP3(BytesIO(file.read()))
    duration = audio.info.length

    return {
        "statusCode": 200,
        "headers": { "Content-Type": "application/json" },
        "body": {
            "duration_seconds": round(duration, 2),
            "duration_formatted": f"{int(duration//60)}m {int(duration%60)}s"
        }
    }
