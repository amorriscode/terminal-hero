from openal import *
import time
import argparse
import th.song

# Parse CLI arguments
parser = argparse.ArgumentParser(description='Bringing musical skills and fast fingers to a terminal near you 🤘')
parser.add_argument('songPath', help='path to your Frets on Fire song')
args = parser.parse_args()

# Create transport and start playing
transport = th.song.Song(args.songPath)
transport.play()

# Wait around while the song is playing
while transport.get_state() == AL_PLAYING:
	time.sleep(1)

# Quit OpenAL after the song is no longer playing
oalQuit()