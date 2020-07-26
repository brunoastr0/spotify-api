import spotipy
import spotipy.oauth2 as so


SPOTIPY_CLIENT_ID='051c0d33d2c44a3c85bd09609b53f88a'
SPOTIPY_CLIENT_SECRET='533b8d03ffa64d2893e7129b65e77824'
SPOTIPY_REDIRECT_URI='http://localhost:8080/callback/'

scope = "user-library-read"

client_credentials_manager = so.SpotifyClientCredentials(SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


def getTrackIDs(user, playlist_id):
    ids = []
    playlist = sp.current_user_playlists(1)
    print(playlist)
    for item in playlist['tracks']['items']:
        track = item['track']
        ids.append(track['id'])
    return ids



ids = getTrackIDs('Melanie Reis', '2oxrg6xFIkHJhVg2cqhAnh')

def getTrackFeatures(id):
  meta = sp.track(id)
  features = sp.audio_features(id)

  # meta
  name = meta['name']
  album = meta['album']['name']
  artist = meta['album']['artists'][0]['name']
  release_date = meta['album']['release_date']
  length = meta['duration_ms']
  popularity = meta['popularity']

  # features
  acousticness = features[0]['acousticness']
  danceability = features[0]['danceability']
  energy = features[0]['energy']
  instrumentalness = features[0]['instrumentalness']
  liveness = features[0]['liveness']
  loudness = features[0]['loudness']
  speechiness = features[0]['speechiness']
  tempo = features[0]['tempo']
  time_signature = features[0]['time_signature']

  track = [name, album, artist, release_date, length, popularity, danceability, acousticness, danceability, energy, instrumentalness, liveness, loudness, speechiness, tempo, time_signature]
  return track

tracks = []
'''for i in range(len(ids)):
  track = getTrackFeatures(ids[i])
  tracks.append(track)
  print(track[1])'''


def getPlaylistId(user):
    ids=[]
    playlist = sp.current_user_playlists(1)
    ids.append(playlist)

    
    print(ids[0])



