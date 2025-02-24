# ETL project
# Step 1: Extract Spotify API 
# Step 2: Transform with pandas and visualize with seaborn
# Step 3: Load data into a S3 bucket
# Goal: find 50 most popular ballad/pop songs from US and UK for each month since 2020 

## Step 1: Spotify API
## Create a Spotify for developers account at https://developer.spotify.com/documentation/web-api
## Create an app and select web API, name ETL_project_3A
## Redirect URI http://localhost:8888/callback

## Step 2: Transform with pandas and visualize with seaborn
## conda activate deploy_env in terminal
#  install and import package
## pip install spotipy in terminal
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
import seaborn as sns
import boto3
from datetime import datetime

## Spotify API credentials
API_CLIENT_ID = "1e4b22ec0a6d42bd94ce4d1f0f28d2af"
API_CLIENT_SECRET = "212c6f6c593c4a6e9df1ebeea8a66dc1"
## Initialize Spotipy API
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id = API_CLIENT_ID, client_secret=API_CLIENT_SECRET))

# Search top 50 US and UK tracks at Spotify 
top50_us = https://open.spotify.com/playlist/37i9dQZEVXbLRQDuF5jeBp
top50_uk = https://open.spotify.com/playlist/37i9dQZEVXbLnolsZ8PSNw
countries = ["US", "UK"]
countries_playlist = {"
                      US":"37i9dQZEVXbLRQDuF5jeBp", 
                      "UK":"37i9dQZEVXbLnolsZ8PSNw"
                      }
# Fetch top 50 tracks by country
for country, playlist in countries_playlist.items:
    results = sp.playlist_tracks(playlist)
    print(f"\nTop 5 Pop Ballads in {country}")