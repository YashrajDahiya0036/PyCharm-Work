# Import the required module for text
# to speech conversion
from gtts import gTTS

# This module is imported so that we can
# play the converted audio
import os

# The text that you want to convert to audio
my_text = 'This is text to mp3 converter.'

# Language in which you want to convert
language = 'en'

# Passing the text and language to the engine,
# here we have marked slow=False. Which tells
# the module that the converted audio should
# have a high speed
my_object = gTTS(text=my_text, lang=language, slow=False)

# Saving the converted audio in a mp3 file named
# welcome
my_object.save("welcome.mp3")

# Playing the converted file
os.system("welcome.mp3")
