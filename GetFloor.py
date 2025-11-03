import requests
import json
import sys

import zlib
import numpy as np
from base64 import b64encode

import time
import threading
import random

url = "http://127.0.0.1:6600"+"/get_floor"
payload = {}
r = requests.post(url, data=json.dumps(payload))  

# 回傳的字串
print(r.text)

# 如果POST的JSON格式沒有錯誤，其指令回傳為JSON資料格式
# 若不是，則上面的輸入格式有誤 
try:
    json_data = r.json()  
    
    '''
    回傳資料格式
    {
        'result':'success',          # 會有'success'和'fail'兩字串，'success'代表console端沒錯誤，'fail'代表console端可能有錯誤
        
        'value':{ 
                    "1F":"map_1F",   # 回傳 "樓層名稱":"對應的地圖名稱"
                    "2F":"map_2F",
                    "3F":"map_3F",
                }
        }
                 
    '''
    
    result = json_data['result']
    print("result=", result)
    print("----------")
    
    floor_dict = json_data['value']
    
    for key in floor_dict:
        print("floor:'{fl}' - map:'{m}' ".format(fl=key, m=floor_dict[key]))
    
            
except:                      
    print("The POST JSON format has error!")                      