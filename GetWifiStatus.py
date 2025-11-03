import requests
import json
import sys

import zlib
import numpy as np
from base64 import b64encode

import time
import threading
import random

url = "http://127.0.0.1:6600"+"/get_wifi_status"
payload = {
            "option":"all",   # "name" - 回傳 '給定名稱' 的wifi連線狀態
                              # "all"  - 回傳 '全部' 的wifi連線狀態 
                                    
            "agv_name": "xxxx"  # 如果option是"all"，則忽略此項目；是"name"，則選擇給定的AGV name            
            
            }
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
        
        'value':         
                 [
                    ["msi_sim1", 1, 0.0]
                 ] 
                
        }        
    '''
    
    result = json_data['result']
    print("result=", result)
    print("----------")
    
    print("agv ==> ")
    print("----------")
 
    agv_list = json_data['value']
    for agv in agv_list:
        print("agv name="                        , agv[0])  # 格式為字串(str)
        print("agv WIFI status="                 , agv[1])  # 格式為int, 1 => 連線中
                                                            #            0 => 斷線中
        print("agv WIFI disconnect duration="    , agv[2])  # 格式為float, 斷線持續的時間

        print("==========")

            
except:                      
    print("The POST JSON format has error!")             