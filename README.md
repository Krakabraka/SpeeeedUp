# SpeeeedUp
Program that you can use to make those "sped up/nightcore" videos

**You need FFmpeg installed! SpeeeedUp runs on Python 3.9!**

## REQUIREMENTS:

numba v0.56.4

pydub v0.25.1

pytube v12.1.3

librosa v0.10.0

## CONFIG

SpeeeedUp has a config. These are the variable names and how to modify them:

Speed Change: How much to pitch shift/speed change. When the value is increased by one, the pitch is shifted 1 semitone higher and the tempo is increased by 8.3%.

Disable Speedup: Disables increasing tempo, leaving only pitch shifting. This is useful if the song is already really fast, but you want to increase the pitch of it. Can be True or False.

Disable Pitch-Shift: Disables shifting pitch, leaving only increasing tempo. Can be True or False.
