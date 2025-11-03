import requests
import json
import sys

import zlib
import numpy as np
from base64 import b64encode

import time
import threading
import random

#透過此API，強制指定的機器人關閉UV燈

url = "http://127.0.0.1:6600"+"/turnoff_uvc"
payload = { 
            "robot_name": "msi_simulator_b",            # 格式為str，指定機器的名字，如果有指定就只會挑選特定名稱的機器                                                                          
          }
r = requests.post(url, data=json.dumps(payload))   
time.sleep(2.0) 

# 回傳的字串
print(r.text)

# 如果POST的JSON格式沒有錯誤，其指令回傳為JSON資料格式
# 若不是，則上面的輸入格式有誤 
try:
    json_data = r.json()  
    

    '''
    回傳資料格式
    {
        'result':'success',          # 'success': 代表命令成功
                                     # 'robot not found': 找不到對應的機器人
        
        'value': 1                   # 格式為int，成功為1，失敗為0
        }        
    '''                        
    
    result = json_data['result']
    print("result=", result)
    print("----------")
    
    value = json_data['value']
    print("value=", value)
    print("----------")
    
            
except:                      
    print("The POST JSON format has error!")  