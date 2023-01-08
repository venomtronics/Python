from gtts import gTTS
import os

text = "நான் தான் மெகாலஷ் ன் உங்களுக்காக என்ன செய்யணும்"
tts = gTTS(text=text,lang="ta")
tts.play()
