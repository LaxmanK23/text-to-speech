from pydub import AudioSegment
import os

# Load all narration segments
segments = []
for i in range(1, 100):  # up to 100 segments
    filename = f"segment_{i}.mp3"
    if os.path.exists(filename):
        segments.append(AudioSegment.from_file(filename))
    else:
        break

narration = sum(segments)

# Load background music
music = AudioSegment.from_file("background.mp3")
music = music - 20
music = music * (len(narration) // len(music) + 1)
music = music[:len(narration)]

# Mix narration with background
final = music.overlay(narration)
final.export("ramayana_chapter_1_mix.mp3", format="mp3")
print("🎧 Final chapter mix saved as ramayana_chapter_1_mix.mp3")
