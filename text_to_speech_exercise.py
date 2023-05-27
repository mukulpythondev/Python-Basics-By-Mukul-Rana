from gtts import gTTS 
import os
l=['Mukul', 'Harry ', 'Uditya']
language = 'en'
for i in l :
    speak=f"Shout Out to {i}"
    speech = gTTS(text = speak, lang = language, slow = False)
    speech.save(f'speak{i}.mp3')
    os.system(f"start speak{i}.mp3")