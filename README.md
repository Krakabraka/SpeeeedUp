# SpeeeedUp

Program that you can use to make those "sped up/nightcore" videos

**You need FFmpeg installed! You need rubberband installed! SpeeeedUp has only been tested for Windows 10 and higher!**

## SETUP

Please run `py -m pip install -r .\requirements.txt` after downloading the files.

Then, download [rubberband](https://breakfastquay.com/files/releases/rubberband-1.9.2-gpl-executable-windows.zip).

Then, download [FFmpeg](https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-essentials.zip).

Add them both to your PATH and you should be good to go. Please open an issue on the GitHub page if you encounter one.

## CONFIG

SpeeeedUp has a config. These are the variable names and how to modify them:

Speed Change: How much to pitch shift/speed change. When the value is increased by one, the pitch is shifted 1 semitone higher and the tempo is increased by 8.3%.

Disable Speedup: Disables increasing tempo, leaving only pitch shifting. This is useful if the song is already really fast, but you want to increase the pitch of it. Can be True or False.

Disable Pitch-Shift: Disables shifting pitch, leaving only increasing tempo. Can be True or False.
