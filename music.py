#!/usr/bin/env python
# -*- coding: utf-8 -*-

html = '''Content-type: text/html;

<html>
<head>
  <meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
  <title>file</title>
</head>
<body>
<h1>曲名(ファイル名)と曲のURLを入力してください</h1>
<form action="music.py" method="post">
      <p>曲名</p><input type="text" name="曲名" /><p>URL</p><input type="text" name="URL" />
  <input type="submit" />
</form>
<p>
  曲名= %s <br>
<p>%s</p>

<form name="formSubmit" action="menu.py">
    <input type="submit" name="button" value="ホームへ戻る">
  </form>
</body>
</html>
'''

import cgi
import os, sys
from tkinter import N
from unicodedata import name
from unittest import result
from matplotlib.pyplot import table
import numpy as np
import pandas as pd
from PIL import Image
import time
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

f = cgi.FieldStorage()
x = f.getfirst("曲名", '')
y = f.getfirst('URL', '')

client_id = '541bd67003d84825981ec2c7ed8e5a10'
client_secret = '2b303fe29f274ea9b89333a0de1ce4e3'


client_credentials_manager = spotipy.oauth2.SpotifyClientCredentials(client_id, client_secret)
spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# 曲のidを設定
result = spotify.audio_features(y)
df = pd.DataFrame(result)
C = ''
df_1 = ''
C = df.to_csv("/Users/tanakashunta/MUDS/人工知能アルゴリズム/last/csv/music_3.csv", sep = ',')
df_1 = df.to_html()


path = 'cgi-bin/name.txt'

with open(path, mode='w') as f:
    f.write(x+'\n')

print(html % (x,df_1))