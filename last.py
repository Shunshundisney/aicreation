#!/usr/bin/env python
# -*- coding: utf-8 -*-

html = '''Content-type: text/html;

<html>
<head>
  <meta http-equiv="Content-Type" content="text/html" charset="UTF-8" />
  <title>ファイルをアップロードする</title>
</head>
<body>
<form name="formSubmit" action="menu.py">
    <input type="submit" name="button" value="ホームへ戻る">
  </form>
<div>
</div>
<h1>%sと似た曲は..</h1>
<p>%s</p>
</body>
</html>
'''

import cgi
import os, sys
from re import X
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

# -*- coding: utf-8 -*-
import pprint
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import time



B = ''
C = ''

#アルバムから取得

df = pd.read_csv("music_1.csv", header=0, index_col=0)
t_name  = df["name"]
B = df.loc[:,["mode","danceability","acousticness","energy","instrumentalness","liveness","loudness","speechiness","tempo","time_signature","valence"]]
a = B.iloc[0].to_numpy()

#曲から取得
df1 = pd.read_csv("csv/music_3.csv", header=0, index_col=0)
C = df1.loc[:,["mode","danceability","acousticness","energy","instrumentalness","liveness","loudness","speechiness","tempo","time_signature","valence"]]

qvec = C.iloc[0].to_numpy()



# コサイン類似度を求める関数
import numpy as np

def comp_sim(qvec,tvec):
    return np.dot(qvec, tvec) / (np.linalg.norm(qvec) * np.linalg.norm(tvec))

D = comp_sim(qvec, B.iloc[0].to_numpy())

result=np.array([])
for i in range(B.index.shape[0]):
    result=np.append(result, comp_sim(qvec, B.iloc[i,:].to_numpy()))

rank = np.argsort(result)
for index in rank[:-rank.shape[0]-1:-1]:
    A_1 = ('{}\t{}'.format(t_name[index], result[index]))

q = pd.DataFrame(data = {'name_path':t_name,'score':result})
z = q.set_index(['name_path','score'])
table = z.to_html()
q.to_csv('/Users/tanakashunta/MUDS/人工知能アルゴリズム/last/csv/rank.csv',mode='w')
#df_2 = q.to_html()

df_2 = q.sort_values('score', ascending=False)
df_3 = df_2.to_html()


with open('cgi-bin/name.txt', 'r') as f:
    last_line = f.readlines()[-1]


print (html % (last_line,df_3))