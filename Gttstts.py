from gtts import gTTs
from playsound import playsound
text="this is gtts module its have many languages "
audio=gTTs(text)
audio.save('exampleaudioofgtts.mp3')
playsound('exampleaudioofgtts.mp3')