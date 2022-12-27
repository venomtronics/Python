import pyttsx3

# Initialize the TTS engine with a specific engine
engine = pyttsx3.init(engine_name='sapi5')

# Set the language to Tamil replace tamil with your language 
engine.setProperty('voice', 'tamil')

# Generate TTS output in Tamil
engine.say('வணக்கம், உலகம்!')

# Run the TTS engine to speak the output
engine.runAndWait()