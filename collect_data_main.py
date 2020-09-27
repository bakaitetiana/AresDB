from urllib.request import Request, urlopen

import requests
import random
import json
import pickle
import time
import os

api_url = 'https://api.um.warszawa.pl/api/action/busestrams_get/?resource_id=%20f2e5503e927d-4ad3-9500-4ab9e55deb59&apikey=eab347a3-4a41-40ee-a895-5bf8e136e89b&type=2'
#Taking response and request  from url
ends = ('th','st','nd','rd','th','th','th','th','th','th')
count = 0
i = 9
n = 0
while(True):
    try:
        while(True):
            r = requests.get(api_url)
            #reading and decoding the data
            data = r.json()
            with open((str(i)+'_data.json'), 'a+') as f:
                json.dump(data, f)
                count+=1
                print(f"\tDebug\tcount is {count}")
                if count >= 1000 :
                  
                    i+=1
                    print(f"100 count new file, now file number {i}")  
                    count = 0              
                  
            

                f.write('\n')
                time.sleep(10)
    except:
        print('')

    n+=1
    s = int(str(n)[-1:])

    print("We're out {}'{} time".format(  count, 
                                            ends[s],
                                        ))