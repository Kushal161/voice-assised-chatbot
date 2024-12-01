import speech_recognition as sr
import wave
import requests
# Initialize the recognizer
recognizer = sr.Recognizer()
try:
    response = requests.get('http://127.0.0.1:5000/audio')
    with open('audio.wav', 'wb') as f:
        f.write(response.content)
        print("audio downloaded successfully")
# Capture audio from the microphone
except Exception as e:
    print("Error:",e)


try:
    audio_file = "audio.wav"
    with sr.AudioFile(audio_file) as source:
        # Recognize speech using Google Speech Recognition
        audio_data = recognizer.record(source)
        text = recognizer.recognize_google(audio_data)
        print("You said: ", text)
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))
