import spotipy
import requests
import json
import spotipy
#import spotipy.oauth2 as so
import cred_token as ss






def getPlaylistId(user, nome):
    playlist = ss.sp.user_playlists(user)
    
    n = len(playlist["items"])
    print(n)
    for i in range(0,n):
        if nome in playlist["items"][i]["name"].lower().strip():
            print(f"[{i}]{playlist['items'][i]['name']}")
    song_name = int(input("Playlist nr: "))
    id = playlist["items"][song_name]["id"]
       

    return id
            




def addSong(Playlist_id,Song_id):
    query = f"https://api.spotify.com/v1/playlists/{Playlist_id}/tracks?uris=spotify%3Atrack%3A{song_id}"
    response = requests.post(
        query,
        headers={
            "Content-Type": "application/json",
            "Authorization": "Bearer {}".format(ss.spotify_token["access_token"])
        }
    )
    response_json = response.json()
    print(response_json)

    

  

def search_Song(song_name):
    
    query = f"https://api.spotify.com/v1/search?q={song_name}&type=track&market=US"
    response = requests.get(
        query,
        headers={
            "Content-Type": "application/json",
            "Authorization": "Bearer {}".format(ss.spotify_token["access_token"])
        }
    )
    response_json = response.json()

    

    n = len(response_json["tracks"].values())
    print("The songs are: ")
    #p = len(response_json['tracks']['items'][i]['album']['artists'])
    for i in range(0,n):
        print(f"[{i}] {response_json['tracks']['items'][i]['name']}",end="")
        print(f" by {response_json['tracks']['items'][i]['album']['artists'][0]['name']}",end="\n")
        

    esco = int(input("chose one: "))
    id = response_json['tracks']['items'][esco]['id']
    return id


name = str(input("Serach for Playlist: "))
id = getPlaylistId(ss.use_name,name)
song_id = search_Song("Ai calica")
addSong(id,song_id)