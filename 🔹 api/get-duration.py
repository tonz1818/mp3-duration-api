from mutagen.mp3 import MP3
from io import BytesIO
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/get-duration', methods=['POST'])
def get_duration():
    file = request.files.get('file')
    if not file:
        return jsonify({'error': 'No file uploaded'}), 400
    audio = MP3(BytesIO(file.read()))
    duration = audio.info.length
    return jsonify({
        'duration_seconds': round(duration, 2),
        'duration_formatted': f"{int(duration//60)}m {int(duration%60)}s"
    })
