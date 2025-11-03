import requests
import json
import sys

import zlib
import numpy as np
from base64 import b64encode

import time
import threading

# 取得規劃路線
url = "http://127.0.0.1:6600"+"/get_elevator"
payload = {}
r = requests.post(url, data=json.dumps(payload))

#print(r.text)

'''
回傳資料格式
{
    'result':'success',          # 會有'success'和'fail'兩字串，'success' 代表任務新增成功
                                 #                              'fail'    代表任務新增失敗
                                 # 
                                 #
                                 
    'value': {'elevator': [
               ["Elevator_D1", ['B1', '1F', '2F', '3F', '5F', '6F', '7F', '8F']], 
               ["Elevator_D2", ['B1', '1F', '2F', '3F', '5F', '6F', '7F', '8F']]    ], 
               
               
              'num': 2
             }             
    }                            
    
             
'''

json_data = r.json()
print("json_data['value']=")
print(json_data['value'])

#print(json_data['value']['elevator'][0][0])
#print(json_data['value']['elevator'][1][0])