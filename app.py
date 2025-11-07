# unreviewed chatgpt code

import requests
import pyttsx3
import base64

# Spotify credentials
CLIENT_ID = 'your_spotify_client_id'
CLIENT_SECRET = 'your_spotify_client_secret'

# function to get spotify access token
def get_access_token():
  auth_url = 'https://accounts.spotify.com/api/...'
  auth_data = {'grant_type': "client_credentials"}
  auth_headers = {
    'Authorization': 'Basic ' + base64.b64encode((CLIENT_ID + ':' + CLIENT_SECRET).encode('utf-8')).decode('utf-8')
  }
  response = requests.post(auth_url, data=auth_data, headers=auth_headers)
  return response.json()['access token']

# Function to get currently playing song
def get_currently_playing_song(access_token):
    url = "https://api.spotify.com/v1/me/player/currently-playing"
    headers = {
        "Authorization": f"Bearer {access_token}"
    }
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        track_name = data['item']['name']
        artists = ', '.join([artist['name'] for artist in data['item']['artists']])
        return track_name, artists
    else:
        return None, None
    
# Function to announce the song using TTS
def announce_song(track_name, artists):
    engine = pyttsx3.init()
    announcement = f"Now playing {track_name} by {artists}"
    engine.say(announcement)
    engine.runAndWait()

if __name__ == "__main__":
    access_token = get_access_token()
    track_name, artists = get_currently_playing_song(access_token)

    if track_name and artists:
        announce_song(track_name, artists)
    else:
        print("No song is currently playing.")
