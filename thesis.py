# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 15:21:58 2020

@author: Tanya
"""

from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import requests
import random
import json
import pickle
import time
import os

api_url = 'https://api.um.warszawa.pl/api/action/busestrams_get/?resource_id=%20f2e5503e927d-4ad3-9500-4ab9e55deb59&apikey=eab347a3-4a41-40ee-a895-5bf8e136e89b&type=2'
#Taking response and request  from url

count = 0
i = 1

try:
    while(True):
        r = requests.get(api_url)
            #reading and decoding the data
        data = r.json()
        with open((str(i)+'_data.json'), 'a+') as f:
            json.dump(data, f)
            for line in f: 
                count += 1
            if count == 10000:
                i+=1
                count = 0
            f.write('\n')
            time.sleep(10)
except:
    print('')

    

    
 
