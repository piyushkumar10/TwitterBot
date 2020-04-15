# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 15:34:36 2020

@author: piyus
"""

import tweepy as tp
import time
import os
#Your developer Account details
consumer_key=""
consumer_secret=""
access_token=""
access_secret=""

auth=tp.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_secret)
api=tp.API(auth)

os.chdir('calm')
for img in os.listdir('.'):
    api.update_with_media(img)
    time.sleep(10)
"""To delete all the tweets of the bots---
for status in tp.Cursor(api.user_timeline).items():
     try:
         api.destroy_status(status.id)
         #print "Deleted:", status.id
     except:
         pass
         #print "Failed to delete:", status.id"""
