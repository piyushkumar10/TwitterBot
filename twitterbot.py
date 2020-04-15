# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 15:34:36 2020

@author: piyus
"""

import tweepy as tp
import time
import os

consumer_key="6JarK1v5kNViMcdpWI7SZKCDM"
consumer_secret="y6WYlBPgGQkHJfneE25DCqN3FAEHKAKSH9XiIYLTaLXvgMLDS5"
access_token="1250350525846974465-0lxCVXBI1s0JcmYrM43e7GrmBWYQBF"
access_secret="iTHWZ2YNGt71x0HfUEioWvr1OgBiKih1iXOEq0sEwLy0U"

auth=tp.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_secret)
api=tp.API(auth)

os.chdir('calm')
for status in tp.Cursor(api.user_timeline).items():
     try:
         api.destroy_status(status.id)
         #print "Deleted:", status.id
     except:
         pass
         #print "Failed to delete:", status.id