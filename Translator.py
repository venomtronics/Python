import googletrans

# Create a Translator object
translator = googletrans.Translator()

# Set the text to translate
text = "Hello, World!"

# Translate the text
translation = translator.translate(text, dest='ta')

# Print the translated text
print(translation.text)
