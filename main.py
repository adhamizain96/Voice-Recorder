#!/usr/bin/env python
# coding: utf-8

# In[1]:


#note - https://python-sounddevice.readthedocs.io/en/0.4.4/
import sounddevice
#note - https://pypi.org/project/wavio/
#---import wavio
#note - https://docs.python.org/3/library/tkinter.html
import soundfile
from tkinter import *

#constants
#---freq = 44100
#time
#---duration = 10

#note - constants always go on the top   
FONT = ('Courier', 15, 'normal')
YELLOW = '#f7f5dd'

def voice_recorder():
    fs = 44100
    #duration = 10
    duration = int(input('How long would you like to record (secs.)?: '))
    #note - https://python-sounddevice.readthedocs.io/en/0.3.7/
    #note - error documentation - https://python-sounddevice.readthedocs.io/en/0.4.4/_modules/sounddevice.html
    sound_recording = sounddevice.rec(int(duration * fs), samplerate = fs, channels = 1)
    sounddevice.wait()
    return soundfile.write('Voice_Recording.flac', sound_recording, fs)
   
#tk() - allows you to register and unregister a callback function which will be called from the Tk mainloop
window = Tk()
window.title('Voice Recorder')
window.geometry('200x55')
#padx & pady - a distance - designating external padding on each side of the slave widget
#fg - foreground color & bg - background color
window.config(padx = 10, pady = 10, bg = YELLOW)

#command calls the play_song function
voice_recording_button = Button(text = 'Record', highlightthickness = 0, command = voice_recorder)
voice_recording_button.config(font = FONT, padx = 5, pady = 5)
voice_recording_button.grid(column = 1 , row = 1)

window.mainloop()   


# In[ ]:




