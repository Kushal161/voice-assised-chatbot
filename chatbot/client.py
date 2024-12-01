import pyaudio
import wave
import requests
import os

# Function to record audio
def record_audio(filename, duration=5, rate=44100, chunk=1024, channels=1):
    audio = pyaudio.PyAudio()

    stream = audio.open(format=pyaudio.paInt16,
                        channels=channels,
                        rate=rate,
                        input=True,
                        frames_per_buffer=chunk)

    print("Recording...")

    frames = []
    for i in range(0, int(rate / chunk * duration)):
        data = stream.read(chunk)
        frames.append(data)

    print("Finished recording.")

    stream.stop_stream()
    stream.close()
    audio.terminate()

    wf = wave.open(filename, 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
    wf.setframerate(rate)
    wf.writeframes(b''.join(frames))
    wf.close()

# Function to send audio file to Flask server
def send_audio_to_server(filename, url):
    files = {'audio': open(filename, 'rb')}
    response = requests.post(url, files=files)
    print("Server response:", response.text)

# Function to retrieve audio file from Flask server and play it
def play_audio_from_server(filename, url):
    response = requests.get(url)
    with open(filename, 'wb') as f:
        f.write(response.content)
    play_audio(filename)

# Function to play audio
def play_audio(filename):
    wf = wave.open(filename, 'rb')

    audio = pyaudio.PyAudio()

    stream = audio.open(format=audio.get_format_from_width(wf.getsampwidth()),
                        channels=wf.getnchannels(),
                        rate=wf.getframerate(),
                        output=True)

    data = wf.readframes(1024)

    while data:
        stream.write(data)
        data = wf.readframes(1024)

    stream.stop_stream()
    stream.close()
    audio.terminate()

if __name__ == "__main__":
    # Modify these variables according to your requirements
    RECORD_FILENAME = 'recorded_audio.wav'
    PLAY_FILENAME = 'played_audio.wav'
    DURATION = 5  # Duration of recording in seconds
    SERVER_URL = 'http://127.0.0.1:5000/audio'  # Flask server URL for retrieving audio

    # Recording and sending audio to server
    record_audio(RECORD_FILENAME, duration=DURATION)
    send_audio_to_server(RECORD_FILENAME, SERVER_URL)

    # Retrieving and playing audio from server
    play_audio_from_server(PLAY_FILENAME, SERVER_URL)
