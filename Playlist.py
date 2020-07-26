import requests
import json
import cred_token as ct


"""Create A New Playlist"""
request_body = json.dumps({
    "name": "Youtube Liked Vids",
    "description": "All Liked Youtube Videos",
    "public":False
})

query = "https://api.spotify.com/v1/users/{}/playlists".format(
    ct.use_name)
response = requests.post(
    query,
    data=request_body,
    headers={
        "Content-Type": "application/json",
        "Authorization": "Bearer {}".format(ct.spotify_token["access_token"])
    }
)
response_json = response.json()

print(response_json)
#print(spotify_token)