# Imports
import soundfile as sf
from pydub import AudioSegment as seg
from pytube import YouTube
import pyrubberband as pyrb
import os

# Config loader
cfg = {}

with open("config.txt", "r") as config:
    for line in config.readlines():
        line = line.split(": ")
        line[1] = line[1].replace("\n", "")

        if line[1].title() == "True":
            cfg[line[0]] = True
        elif line[1].title() == "False":
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
    print("File \"input.mp3\" detected; skipping downloading stage!")
    title = "output"
    os.replace("input.mp3", "original.mp3")

else:
    link = input("Paste YouTube URL to speed up: ")
    try:
        # This code downloads the video
        link = YouTube(link)
        print("Downloading video... ")
        link = link.streams.filter(only_audio=True).first()
        link.download()

        # Replaces the mp4 downloaded file with an mp3
        title = removeIllegalChars(link.title)
        os.replace(title + ".mp4", "original.mp3")

    except:
        print("That's not a valid URL!")
        quit(0)

# Load the file
print("Loading audio... ")

# Convert the mp3 to a wav because soundfile is a b**ch
try: a = seg.from_file("original.mp3", "mp3")
except: a = seg.from_file("original.mp3", "mp4") # some files are formatted as mp3's and some are mp4's so this try-except is here to fix that
a.export("original.wav", format="wav")

os.remove("original.mp3")
y, sr = sf.read("original.wav")

print("Modifying audio... ")
if not cfg.get("Disable Speedup"): y = pyrb.time_stretch(y, sr, 1+(cfg.get("Speed Change")/12))
if not cfg.get("Disable Pitch-Shift"): y = pyrb.pitch_shift(y, sr, cfg.get("Speed Change"))

print("Writing to file... ")

# Export the file
sf.write(f"{title}.wav", y, sr)
os.remove("original.wav")
print(f"Saved as {title}.wav.")
