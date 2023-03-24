# Import Translator class from googletrans module
from googletrans import Translator

# Create an instance of Translator
translator = Translator()

# Translate a text from Korean to Japanese
result = translator.translate('안녕하세요.', dest='ja')

# Print the translated text and other information
print(result.text) # こんにちは。
print(result.src) # ko
print(result.dest) # ja

# Detect the language of a text
result = translator.detect('This sentence is written in English.')

# Print the detected language and confidence score
print(result.lang) # en
print(result.confidence) # 0.22348526