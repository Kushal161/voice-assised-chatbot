import speech_recognition as sr

# Initialize the recognizer
recognizer = sr.Recognizer()

# Path to your WAV audio file
audio_file_path = "played_audio.wav"

# Load the audio file
with sr.AudioFile(audio_file_path) as source:
    audio_data = recognizer.record(source)  # Read the entire audio file

try:
    # Recognize speech using Google Speech Recognition
    text = recognizer.recognize_google(audio_data)
    print("Transcription: ", text)
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))
