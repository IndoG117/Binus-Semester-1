# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 12:59:57 2019

@author: Gadtardi Wongkaren
"""

#%%
import json
from datetime import datetime

with open(r'C:\Users\Djagad P. Dwialam\Documents\tweet1.txt') as json_file:
    data_list = json.load(json_file)

print(data_list)
timestamp = time.time()
dt_object = datetime.fromtimestamp(timestamp)

newtweet = input('insert new tweet:')
data_list['text'] = newtweet
data_list['created_at'] = str(dt_object)


with open(r'C:\Users\Djagad P. Dwialam\Documents\tweetout.txt', 'w+') as outfile:
    json.dump(data_list, outfile, indent = 4)