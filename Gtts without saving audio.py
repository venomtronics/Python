from gtts import gTTS
import os

text = "Hello, this is a test of the gTTS library"
tts = gTTS(text=text)
tts.play()
