from sneak import *
import os
os.add_dll_directory("C:\Program Files\VideoLAN\VLC")
import vlc

p=vlc.MediaPlayer(list_files("res/")[0])
p.play()
