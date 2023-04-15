# Imports
from pydub import AudioSegment
from pytube import YouTube
import numpy as np
import librosa.effects as e
import os

# Config loader
cfg = {}

with open("config.txt", "r") as config:
    for line in config.readlines():
        line = line.split(": ")

        if line[1] == "True":
            cfg[line[0]] = True
        elif line[1] == "False":
            cfg[line[0]] = False
        else:
            cfg[line[0]] = float(line[1])

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
    title = "output"
    os.replace("input.mp3", "original.mp3")

else:
    link = input("Paste YouTube URL to speed up: ")
    try:
        # This code downloads the video
        link = YouTube(link)
        print("Downloading... (1/3)")
        link = link.streams.filter(only_audio=True).first()
        link.download()

        # Replaces the mp4 downloaded file with an mp3
        title = removeIllegalChars(link.title)
        os.replace(title + ".mp4", "original.mp3")

    except:
        print("That's not a valid URL!")
        quit(0)

print("Speeding up... (2/3)")
# Load the file
try: a = AudioSegment.from_file("original.mp3", "mp3")
except: a = AudioSegment.from_file("original.mp3", "mp4")
# I have no idea how this code works, I copied it from the internet (https://stackoverflow.com/a/70528584/19847351) but it pitch-shifts the audio
y = np.frombuffer(a._data, dtype=np.int16).astype(np.float32)/2**15
if not cfg.get("Disable Pitch-Shift"): y = e.pitch_shift(y, sr=a.frame_rate*2, n_steps=cfg.get("Speed Change"))
if not cfg.get("Disable Speedup"): y = e.time_stretch(y, rate=1+(cfg.get("Speed Change")/12))
a = AudioSegment(np.array(y * (1<<15), dtype=np.int16).tobytes(), frame_rate = a.frame_rate*2, sample_width=2, channels = 1)

print("Writing to file... (3/3)")

# Export the file
a.export(f"{title}.mp3", format="mp3")
os.remove("original.mp3")
print(f"Saved as {title}.mp3.")
