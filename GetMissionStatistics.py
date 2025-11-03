import requests
import json
import sys

import zlib
import numpy as np
from base64 import b64encode

import time
import threading
import random

url = "http://127.0.0.1:6600"+"/get_mission_statistics"
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
        
        'value':{'unfinish':         # 有'unfinish'和'finish'兩種字串，端看當時POST的'category' 
                 [
                    ['3',  '2/2', 'Simulator_104', '1592209639', '60 sec', '[15938,1592209639]', '[-1,-1.0]', '0', '[0 0 0]', "[[-19.1, 28.48, -3.14, '1F'], [-5.04, 3.66, -0.0, '1F']]", 'none', "1F","50","3"], 
                    ['5', '-1/2', 'Simulator_104', '1592209639', '60 sec', '[15938,1592209639]', '[-1,-1.0]', '0', '[0 0 0]', "[[-19.1, 28.48, -3.14, '1F'], [-5.04, 3.66, -0.0, '1F']]", 'none', "2F","40","4"]
                 ] 
                }
        }     
    '''
    
    result = json_data['result']
    print("result=", result)

            
except:                      
    print("The POST JSON format has error!")                      