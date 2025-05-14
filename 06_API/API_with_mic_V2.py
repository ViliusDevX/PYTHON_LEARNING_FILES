import requests
import pyaudio
import base64
import json


class PyShazam:
    HEADERS = {
        "X-RapidAPI-Key": "MY API KEY WAS HERE",
        "X-RapidAPI-Host": "shazam.p.rapidapi.com"
    }

    @staticmethod
    def record_audio(seconds):
        audio = pyaudio.PyAudio()

        stream = audio.open(format=pyaudio.paInt16,
                            channels=1,
                            rate=44100,
                            frames_per_buffer=1024,
                            input=True)

        frames = []

        for i in range(0, int(44100 / 1024 * seconds)):
            data = stream.read(1024)
            frames.append(data)

        stream.stop_stream()
        stream.close()
        audio.terminate()

        audio_data = b''.join(frames)
        audio_base64 = base64.b64encode(audio_data).decode('utf-8')

        return audio_base64

    @staticmethod
    def detect_song():
        URL = "https://shazam.p.rapidapi.com/songs/v2/detect"
        audio_base64 = PyShazam.record_audio(5)
        payload = {"audio": {"data": {"type": "audio/mpeg", "value": audio_base64}}}

        response = requests.post(URL, headers=PyShazam.HEADERS, json=payload)
        data = response.json()

        songs = [song["title"] for song in data.get("matches", [])]

        return songs


recognized_songs = PyShazam.detect_song()
print(recognized_songs)
