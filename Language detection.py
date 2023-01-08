import googletrans

translator = googletrans.Translator()
result = translator.detect("how are you")
#repalce "how are you" with your language sentance 

print(result.lang)
