from gtts import gTTS
import os
from llm_mistral import B
# Text to be converted to speech
#text = "Hello, how are you today?"

# Language in which you want to convert
language = 'hi'

# Passing the text and language to the engine
tts = gTTS(text=B, lang=language, slow=False)

# Save the converted audio to a file
tts.save("output.wav")

# Play the converted audio
os.system("start output.wav")
