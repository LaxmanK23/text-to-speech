from pydub import AudioSegment
import os

chapter = "ramayana_ch2"
segment_folder = f"output/{chapter}"
output_file = f"{chapter}_episode.mp3"

# Load background music
background = AudioSegment.from_file("background.mp3") - 20

# Load all segments
segments = []
for i in range(1, 100):  # assume max 100 segments
    file_path = f"{segment_folder}/segment_{i}.mp3"
    if os.path.exists(file_path):
        segments.append(AudioSegment.from_file(file_path))
    else:
        break

# Check if we have any narration segments
if not segments:
    print("❗ No narration segments found. Did you generate narration first?")
    exit()

# Combine all narration segments
narration = segments[0]
for segment in segments[1:]:
    narration += segment

# Loop background music to match narration length
bg_loop = background * (len(narration) // len(background) + 1)
bg_loop = bg_loop[:len(narration)]

# Mix voice over music
final_mix = bg_loop.overlay(narration)

# Export
final_mix.export(output_file, format="mp3")
print(f"✅ Final episode saved as: {output_file}")
