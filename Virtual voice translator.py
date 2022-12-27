import speech_rrcognition as sr
import googletrans
translator=googketrans.Translator()
r=sr.Recognizer()
yourlang=input(str("which language you are speaking,enter your language:"))
translang=input(str("enter needed language:"))
while True:
    with sr.Microphone() as source:
      try:
        audio=r.listen(source)
        text=r.recognize_google(audio,yourlang)
        translation=translator.translate(text,dest=translang)
        print("you said ",text,"and translation is",translation.text)
        
        
        