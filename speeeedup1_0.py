# Imports
from pydub import AudioSegment
from pytube import YouTube
import os


# These characters can't be in file names
def removeIllegalChars(j):
    j = j.replace("/", "")
    j = j.replace("\\", "")
    j = j.replace(":", "")
    j = j.replace("*", "")
    j = j.replace("?", "")
    j = j.replace('"', "")
    j = j.replace("<", "")
    j = j.replace(">", "")
    j = j.replace("|", "")
    return j


if os.path.exists("input.mp3"):
    print("File \"input.mp3\" detected; skipping stage 1!")
    os.replace("input.mp3", "original.mp3")

else:
    link = input("Paste YouTube URL to speed up: ")

    # This code downlaods the video
    print("Downloading... (1/3)")
    link = YouTube(link)
    link = link.streams.filter(only_audio=True).first()
    link.download()
    # Replaces the mp4 downloaded file to an mp3
    title = removeIllegalChars(link.title)
    os.replace(title + ".mp4", "original.mp3")

print("Speeding up... (2/3)")
# Load the file
try: a = AudioSegment.from_file("original.mp3", "mp3")
except: a = AudioSegment.from_file("original.mp3", "mp4")

pitch_increase = 0.2  # Change this if you want to increase the pitch more or less
# I have no idea how this code works, I copied it from the internet but it speeds up the audio
new_sample_rate = int(a.frame_rate * (2.0 ** pitch_increase))
a = a._spawn(a.raw_data, overrides={'frame_rate': new_sample_rate})
a = a.set_frame_rate(44100)

print("Writing to file... (3/3)")

# Export the file
a.export(f"{title}.mp3", format="mp3")
os.remove("original.mp3")
print(f"Saved as {title}.mp3.")
