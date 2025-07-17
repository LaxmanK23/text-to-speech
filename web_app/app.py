import os
import asyncio
from flask import Flask, request, render_template, send_file
import edge_tts
from pydub import AudioSegment

UPLOAD_FOLDER = "uploads"
OUTPUT_FOLDER = "output"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

app = Flask(__name__)

def parse_uploaded_file(path):
    segments = []
    voice = None
    text = []
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line.startswith("[") and line.endswith("]"):
                if voice and text:
                    segments.append((voice, " ".join(text)))
                    text = []
                voice = line.strip("[]")
            elif line:
                text.append(line)
        if voice and text:
            segments.append((voice, " ".join(text)))
    return segments

async def generate_tts_segments(segments, output_path):
    all_audio = AudioSegment.silent(duration=0)
    for i, (voice, text) in enumerate(segments, 1):
        filename = os.path.join(OUTPUT_FOLDER, f"segment_{i}.mp3")
        tts = edge_tts.Communicate(text=text, voice=voice)
        await tts.save(filename)
        seg = AudioSegment.from_file(filename)
        all_audio += seg + AudioSegment.silent(duration=500)
    all_audio.export(output_path, format="mp3")
    return output_path

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        file = request.files.get("story")
        if not file:
            return "No file uploaded"

        input_path = os.path.join(UPLOAD_FOLDER, file.filename)
        output_path = os.path.join(OUTPUT_FOLDER, f"narration_{file.filename}.mp3")
        file.save(input_path)

        segments = parse_uploaded_file(input_path)
        asyncio.run(generate_tts_segments(segments, output_path))

        return send_file(output_path, as_attachment=True)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
