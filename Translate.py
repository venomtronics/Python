import googletrans

translator = googletrans.Translator()
result = translator.translate("Hello, world!", dest="fr")

print(result.text)
