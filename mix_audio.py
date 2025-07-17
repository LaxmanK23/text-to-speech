from pydub import AudioSegment

narration = AudioSegment.from_file("narration.mp3")
background = AudioSegment.from_file("background.mp3")

# Reduce background music volume and loop it
background = background - 18  # lower volume
background = background * (len(narration) // len(background) + 1)
background = background[:len(narration)]

# Overlay voice on background
final_mix = background.overlay(narration)

# Export final podcast episode
final_mix.export("podcast_episode.mp3", format="mp3")
print("🎧 Final mix saved as podcast_episode.mp3")
