import spotipy
import spotipy.oauth2 as so


SPOTIPY_CLIENT_ID='051c0d33d2c44a3c85bd09609b53f88a'
SPOTIPY_CLIENT_SECRET='533b8d03ffa64d2893e7129b65e77824'
SPOTIPY_REDIRECT_URI='http://localhost:8080/callback/'
use_name = "melaniiesofia"
#muda

scope = ["playlist-modify-private"]

spotify_token = so.SpotifyOAuth(SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET,SPOTIPY_REDIRECT_URI,None,scope[0],None,use_name).get_access_token()
client_credentials_manager = so.SpotifyClientCredentials(SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

