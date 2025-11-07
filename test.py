import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

CLIENT_ID = "bb8477591680446887bad33cd7229cf7"
CLIENT_SECRET = "f27bae356dbb461b95c7bbf71a956517"
redirectURI = "http://localhost:8888/callback"
scope = "user-read-currently-playing"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, redirect_uri=redirectURI, scope=scope))
last_playing_song = None
last_song = None

while True:
    current_track_data = sp.currently_playing()
    if (current_track_data is None):
        print("No track is currently playing.")
    else:
        song = current_track_data['item']['name']
        artist = current_track_data['item']['artists'][0]['name']
        if (song != last_song):
            print(f"Now playing {song} by {artist}")
        last_song = song
        
        last_playing_song = current_track_data

# Getting Image
img_data = current_track_data['item']['album']['images'][0]['url']
image = requests.get(img_data).content
with open("album.jpg", "wb") as fh:
    fh.write(image)