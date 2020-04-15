# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 00:26:44 2020

@author: piyus
"""
import requests
from bs4 import BeautifulSoup
import os
url="https://unsplash.com/s/photos/calm"
pex=requests.get(url)
print(pex.status_code)
soup=BeautifulSoup(pex.text,'html.parser')
image_tags=soup.findAll('img')
print(image_tags)
if not os.path.exists('calm'):
    os.makedirs('calm')
os.chdir('calm')
x=0
for img in image_tags:
    try:
        url=img['src']
        imgsrc=requests.get(url)
        if imgsrc.status_code==200:
            with open('calm-'+str(x)+'.jpg','wb') as f:
                f.write(requests.get(url).content)
                f.close()
                x+=1
    except:
        pass