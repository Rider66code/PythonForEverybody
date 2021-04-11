#Just a check now, DPAD only

import argparse
import subprocess
import json
import os

def keypress(x):
    tbdval=0
    console = subprocess.Popen(['adb','shell','input','keyboard','keyevent',x], shell=True)
    return tbdval

__author__ = 'S.D.A.'
__version__ = '0.0.1'
__date__ = '2021-04-11'

here = os.path.dirname(os.path.abspath(__file__))
config_file = os.path.join(here, 'adb_rcu_cli.json')
try:
    with open(config_file) as f:
        config = json.load(f)
except:
    print('adb_rcu_cli.json file not found or not correct, exiting.')
    quit()
print('Configuration file found:',config_file)
KB_KEYCODE_DPAD_UP=config["KB_KEYCODE_DPAD_UP"]
KB_KEYCODE_DPAD_DOWN=config["KB_KEYCODE_DPAD_DOWN"]
KB_KEYCODE_DPAD_LEFT=config["KB_KEYCODE_DPAD_LEFT"]
KB_KEYCODE_DPAD_RIGHT=config["KB_KEYCODE_DPAD_RIGHT"]
KB_KEYCODE_MENU=config["KB_KEYCODE_MENU"]
KB_KEYCODE_INFO=config["KB_KEYCODE_INFO"]
KB_KEYCODE_ESCAPE=config["KB_KEYCODE_ESCAPE"]
KB_KEYCODE_BACK=config["KB_KEYCODE_BACK"]
KB_KEYCODE_GUIDE=config["KB_KEYCODE_GUIDE"]
KB_KEYCODE_VOLUME_UP=config["KB_KEYCODE_VOLUME_UP"]
KB_KEYCODE_VOLUME_DOWN=config["KB_KEYCODE_VOLUME_DOWN"]
KB_KEYCODE_CHANNEL_UP=config["KB_KEYCODE_CHANNEL_UP"]
KB_KEYCODE_CHANNEL_DOWN=config["KB_KEYCODE_CHANNEL_DOWN"]
KB_KEYCODE_BUTTON_SELECT=config["KB_KEYCODE_BUTTON_SELECT"]
KB_KEYCODE_DPAD_CENTER=config["KB_KEYCODE_DPAD_CENTER"]
KB_KEYCODE_MEDIA_REWIND=config["KB_KEYCODE_MEDIA_REWIND"]
KB_KEYCODE_MEDIA_FAST_FORWARD=config["KB_KEYCODE_MEDIA_FAST_FORWARD"]
KB_KEYCODE_MEDIA_STOP=config["KB_KEYCODE_MEDIA_STOP"]
KB_KEYCODE_MEDIA_PAUSE=config["KB_KEYCODE_MEDIA_PAUSE"]
KB_KEYCODE_MEDIA_PLAY=config["KB_KEYCODE_MEDIA_PLAY"]
KB_KEYCODE_MEDIA_PLAY_PAUSE=config["KB_KEYCODE_MEDIA_PLAY_PAUSE"]
KB_KEYCODE_MEDIA_RECORD=config["KB_KEYCODE_MEDIA_RECORD"]
KB_KEYCODE_MUTE=config["KB_KEYCODE_MUTE"]
KB_KEYCODE_VOLUME_MUTE=config["KB_KEYCODE_VOLUME_MUTE"]
KB_KEYCODE_CAPTIONS=config["KB_KEYCODE_CAPTIONS"]
KB_KEYCODE_PROG_RED=config["KB_KEYCODE_PROG_RED"]
KB_KEYCODE_PROG_GREEN=config["KB_KEYCODE_PROG_GREEN"]
KB_KEYCODE_PROG_YELLOW=config["KB_KEYCODE_PROG_YELLOW"]
KB_KEYCODE_PROG_BLUE=config["KB_KEYCODE_PROG_BLUE"]
KB_KEYCODE_DVR=config["KB_KEYCODE_DVR"]
KB_KEYCODE_TV_RADIO_SERVICE=config["KB_KEYCODE_TV_RADIO_SERVICE"]

while True:
    name = input("Enter the key or command:\n")
    if name==KB_KEYCODE_DPAD_UP:
        keypress('KEYCODE_DPAD_UP')

    elif name==KB_KEYCODE_DPAD_DOWN:
        keypress('KEYCODE_DPAD_DOWN')

    elif name==KB_KEYCODE_DPAD_LEFT:
        keypress('KEYCODE_DPAD_LEFT')

    elif name==KB_KEYCODE_DPAD_RIGHT:
        keypress('KEYCODE_DPAD_RIGHT')

    elif name==KB_KEYCODE_DPAD_RIGHT:
        keypress('KEYCODE_DPAD_RIGHT')

    elif name==KB_KEYCODE_MENU:
        keypress('KEYCODE_MENU')

    elif name==KB_KEYCODE_INFO:
        keypress('KEYCODE_INFO')

    elif name==KB_KEYCODE_ESCAPE:
        keypress('KEYCODE_ESCAPE')

    elif name==KB_KEYCODE_BACK:
        keypress('KEYCODE_BACK')

    elif name==KB_KEYCODE_GUIDE:
        keypress('KEYCODE_GUIDE')

    elif name==KB_KEYCODE_VOLUME_UP:
        keypress('KEYCODE_VOLUME_UP')

    elif name==KB_KEYCODE_VOLUME_DOWN:
        keypress('KEYCODE_VOLUME_DOWN')

    elif name==KB_KEYCODE_CHANNEL_UP:
        keypress('KEYCODE_CHANNEL_UP')

    elif name==KB_KEYCODE_CHANNEL_DOWN:
        keypress('KEYCODE_CHANNEL_DOWN')

    elif name==KB_KEYCODE_BUTTON_SELECT:
        keypress('KEYCODE_BUTTON_SELECT')

    elif name==KB_KEYCODE_DPAD_CENTER:
        keypress('KEYCODE_DPAD_CENTER')

    elif name==KB_KEYCODE_MEDIA_REWIND:
        keypress('KEYCODE_MEDIA_REWIND')

    elif name==KB_KEYCODE_MEDIA_FAST_FORWARD:
        keypress('KEYCODE_MEDIA_FAST_FORWARD')

    elif name==KB_KEYCODE_MEDIA_STOP:
        keypress('KEYCODE_MEDIA_STOP')

    elif name==KB_KEYCODE_MEDIA_PAUSE:
        keypress('KEYCODE_MEDIA_PAUSE')

    elif name==KB_KEYCODE_MEDIA_PLAY:
        keypress('KEYCODE_MEDIA_PLAY')

    elif name==KB_KEYCODE_MEDIA_PLAY_PAUSE:
        keypress('KEYCODE_MEDIA_PLAY_PAUSE')

    elif name==KB_KEYCODE_MEDIA_RECORD:
        keypress('KEYCODE_MEDIA_RECORD')

    elif name==KB_KEYCODE_MUTE:
        keypress('KEYCODE_MUTE')

    elif name==KB_KEYCODE_VOLUME_MUTE:
        keypress('KEYCODE_VOLUME_MUTE')

    elif name==KB_KEYCODE_CAPTIONS:
        keypress('KB_KEYCODE_CAPTIONS')

    elif name==KB_KEYCODE_PROG_RED:
        keypress('KEYCODE_PROG_RED')

    elif name==KB_KEYCODE_PROG_GREEN:
        keypress('KEYCODE_PROG_GREEN')

    elif name==KB_KEYCODE_PROG_YELLOW:
        keypress('KEYCODE_PROG_YELLOW')

    elif name==KB_KEYCODE_PROG_BLUE:
        keypress('KEYCODE_PROG_BLUE')

    elif name==KB_KEYCODE_DVR:
        keypress('KEYCODE_DVR')

    elif name==KB_KEYCODE_TV_RADIO_SERVICE:
        keypress('KEYCODE_TV_RADIO_SERVICE')

    elif name=='exit':
        break

    else:
        print ('Unrecognized option.')
