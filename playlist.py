#!/usr/bin/env python
# -*- coding: utf-8 -*-

html = '''Content-type: text/html;


<html>
<head>
  <meta http-equiv="Content-Type" content="text/html" charset="UTF-8" />
  <title>ファイルをアップロードする</title>
</head>
<body>
<form method="POST" action="playlist.py">
    <p>プレイリストID</p><input type="text" name="text" />
  <input type="submit" />
</form>
<div>
<form name="formSubmit" action="menu.py">
    <input type="submit" name="button" value="ホームへ戻る">
  </form>
</div>
<p>%s</p>
<p>%s</p>
</body>
</html>
'''

import cgi
import os, sys
from unicodedata import name
from unittest import result
from matplotlib.pyplot import table
import numpy as np
import pandas as pd
from PIL import Image
try:
    import msvcrt
    msvcrt.setmode(0, os.O_BINARY)
    msvcrt.setmode(1, os.O_BINARY)
except ImportError:
    pass
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pprint
import pandas as pd
import time

form = cgi.FieldStorage()
x = form.getfirst("text", '')

client_id = '541bd67003d84825981ec2c7ed8e5a10'
client_secret = '2b303fe29f274ea9b89333a0de1ce4e3'
client_credentials_manager = SpotifyClientCredentials(client_id, client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

def getTrackIDs(user, playlist_id):
    ids = []
    playlist = sp.user_playlist(user, playlist_id)
    for item in playlist['tracks']['items']:
        track = item['track']
        ids.append(track['id'])
    return ids

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
    mode = features[0]['mode']
    liveness = features[0]['liveness']
    loudness = features[0]['loudness']
    speechiness = features[0]['speechiness']
    tempo = features[0]['tempo']
    time_signature = features[0]['time_signature']
    valence = features[0]['valence']

    track = [name, album, artist, release_date, length, mode, popularity, danceability, acousticness, energy, instrumentalness, liveness, loudness, speechiness, tempo, time_signature, valence]
    return track


# 初回ロード時
if form.list == []:
    ids = getTrackIDs('a5h4jvqpjuqia6ll4ejjevgs','37i9dQZEVXbKXQ4mDTEBXq')
    z = "デフォルトで日本のTOP50を表示しています。"
else:
   ids = getTrackIDs('a5h4jvqpjuqia6ll4ejjevgs',x)
   z = "あなたが選んだプレイリストが表示されます"
   
# loop over track ids
tracks = []
for i in range(len(ids)):
    time.sleep(.5)
    track = getTrackFeatures(ids[i])
    tracks.append(track)


#df = pd.DataFrame(tracks)
df = pd.DataFrame(tracks, columns = ['name', 'album', 'artist', 'release_date', 'length', 'mode', 'popularity', 'danceability', 'acousticness', 'energy', 'instrumentalness', 'liveness', 'loudness', 'speechiness', 'tempo', 'time_signature', 'valence'])
C = ''
df_1 = ''
C = df.to_csv("/Users/tanakashunta/MUDS/人工知能アルゴリズム/last/music_1.csv", sep = ',')
df_1 = df.to_html()

print(html % (z,df_1))