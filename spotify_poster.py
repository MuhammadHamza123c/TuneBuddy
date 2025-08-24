import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv
import os
load_dotenv()
client_id = os.environ('client_id')
client_secret = os.environ('client_secret')
auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(auth_manager=auth_manager)
def get_poster(song:str):
    results = sp.search(q=song, type='track', limit=1)
    track = results['tracks']['items'][0]
    poster_url = track['album']['images'][0]['url'] 
    return poster_url


