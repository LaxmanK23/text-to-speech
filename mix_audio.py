# from pydub import AudioSegment

# narration = AudioSegment.from_file("narration.mp3")
# background = AudioSegment.from_file("background.mp3")

# # Reduce background music volume and loop it
# background = background - 18  # lower volume
# background = background * (len(narration) // len(background) + 1)
# background = background[:len(narration)]

# # Overlay voice on background
# final_mix = background.overlay(narration)

# # Export final podcast episode
# final_mix.export("podcast_episode.mp3", format="mp3")
# print("🎧 Final mix saved as podcast_episode.mp3")


from pydub import AudioSegment

def change_playback_speed(sound, speed=1.0):
    # Changing frame rate = changes speed and pitch
    new_frame_rate = int(sound.frame_rate * speed)
    return sound._spawn(sound.raw_data, overrides={'frame_rate': new_frame_rate}).set_frame_rate(sound.frame_rate)

# Load files
narration = AudioSegment.from_file("narration.mp3")
background = AudioSegment.from_file("background.mp3")

# Slow down background music (e.g., to 80% speed)
background = change_playback_speed(background, speed=0.9)

# Reduce volume and loop
background = background - 14  # lower volume
background = background * (len(narration) // len(background) + 1)
background = background[:len(narration)]

# Mix and export
final_mix = background.overlay(narration)
final_mix.export("podcast_episode.mp3", format="mp3")
print("🎧 Final mix saved as podcast_episode.mp3")
