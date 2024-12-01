import speech_recognition as sr
import wave
import requests
# Initialize the recognizer
recognizer = sr.Recognizer()

# Capture audio from the microphone
with sr.Microphone() as source:
    print("Recording...")
    try:
        audio = recognizer.listen(source,phrase_time_limit=4)
        print("Recording done")
    except sr.WaitTimeoutError:
        print("No speech detected. Timeout reached.")
    except Exception as e:
        print("An error occurred:", e)
try:
    # Recognize speech using Google Speech Recognition
    text = recognizer.recognize_google(audio)
    print("You said: ", text)
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))
