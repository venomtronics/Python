import speech_recognition as sr

# Create a SpeechRecognizer object
r = sr.Recognizer()

# Prompt the user to speak a math expression
print("Please speak a math expression:")

# Listen for user input and convert it to text
with sr.Microphone() as source:
    audio = r.listen(source)
    text = r.recognize_google(audio)

# Evaluate the math expression and print the result
result = eval(text)
print(f"The result of the expression is: {result}")
