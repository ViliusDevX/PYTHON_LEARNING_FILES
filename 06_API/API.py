import requests
import pyaudio
import base64
import json

#checking PyShazam class

class PyShazam:
    HEADERS = {
        "X-RapidAPI-Key": "MY API KEY WAS HERE",
        "X-RapidAPI-Host": "shazam.p.rapidapi.com"
    }

    @staticmethod
    def search_tracks(term):
        URL = "https://shazam.p.rapidapi.com/search"
        querystring = {"term": term, "locale": "en-US", "offset": "0", "limit": "5"}
        response = requests.get(URL, headers=PyShazam.HEADERS, params=querystring)
        data = response.json()
        tracks = []

        hits = data.get("tracks", {}).get("hits", [])

        for hit in hits:
            tracks.append(hit["track"]["title"])

        return tracks


song_names = PyShazam.search_tracks("kiss the rain")
print(song_names)
