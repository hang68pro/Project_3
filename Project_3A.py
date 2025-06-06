# ETL project
# Step 1: Extract Spotify API 
# Step 2: Transform with pandas and visualize with seaborn
# Step 3: Load data into a S3 bucket
# Goal: find 5 most popular ballad/pop songs from a testing api on spotify 

## Step 1: Spotify API
## Create a Spotify for developers account at https://developer.spotify.com/documentation/web-api
## Create an app and select web API, name ETL_project_3A
## Redirect URI http://localhost:8888/callback

## Step 2: Transform with pandas and visualize with seaborn
## conda activate deploy_env in terminal
#  install and import package
## pip install spotipy in terminal
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import pandas as pd
import seaborn as sns
import boto3
from datetime import datetime

## Spotify API credentials
API_CLIENT_ID = "1e4b22ec0a6d42bd94ce4d1f0f28d2af"
API_CLIENT_SECRET = "212c6f6c593c4a6e9df1ebeea8a66dc1"
redirect_uri = "http://localhost:8888/callback"

## Initialize Spotipy API
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id = API_CLIENT_ID, client_secret=API_CLIENT_SECRET, 
                                               redirect_uri=redirect_uri,
                                               scope="playlist-read-private playlist-read-collaborative"))

#print("Access Token:", sp.auth_manager.get_access_token(as_dict=False))

# Use Spotify Web API testing playlist
sp_list = sp.playlist(playlist_id='3cEYpjA9oz9GiPac4AsH4n')
print(sp_list.keys())
print(sp_list["tracks"].keys())
tracks = sp_list["tracks"].get("items")

# Create a DataFrame from the track data
df = pd.DataFrame([{
    "track_name": track["track"]["name"],
    "artist": track["track"]["artists"][0]["name"],  # First artist
    "popularity": track["track"]["popularity"],
    "album": track["track"]["album"]["name"],
    "release_date": track["track"]["album"]["release_date"]
} for track in tracks if "track" in track and "popularity" in track["track"]])

# Find the most popular track in this playlist
mostpopular_track = df[df["popularity"] == df["popularity"].max()]
print(mostpopular_track)

