from gtts import gTTS
import os
from llm_mistral import B
import requests
# Text to be converted to speech
#text = "Hello, how are you today?"
from client import play_audio
# Language in which you want to convert
language = 'hi'

# Passing the text and language to the engine
tts = gTTS(text=B, lang=language, slow=False)


# Save the converted audio to a file
tts.save("output.wav")

#sending the file to flask
try:
    files = {'audio': open("output.wav", 'rb')}
    response = requests.post("http://127.0.0.1:5000/audio", files=files)
    print("Server response:", response.text)

except Exception as e:
    print("Error:",e)

response = requests.get("http://127.0.0.1:5000/audio")
with open("abc.wav", 'wb') as f:
    f.write(response.content)
play_audio("abc.wav")

# Play the converted audio
os.system("start output.wav")
