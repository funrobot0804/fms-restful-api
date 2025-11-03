import requests
import json
import sys

import zlib
import numpy as np
from base64 import b64encode

import time
import threading
import random

url = "http://127.0.0.1:6600"+"/get_dock"
payload = {
            "option":"all",   # "name" - 回傳 '給定名稱' 的充電站狀態
                              # "all"  - 回傳 '全部' 的充電站狀態                       
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
        
        'value':{'dock':         
                 [
                    [
                     ["dock_0",-6.16,6.8,-0.0,"1F"]
                     ] 
                 ] 
                }
        }        
    '''
    
    result = json_data['result']
    print("result=", result)
    print("----------")
    
    print("dock ==> ")
    print("----------")
 
    dock_list = json_data['value']['dock']
    for dock in dock_list:
        print("dock name="   , dock[0]) # 格式為字串(str)
        print("dock x="      , dock[1]) # 格式為float，地圖座標，單位為m
        print("dock y="      , dock[2]) # 格式為float，地圖座標，單位為m
        print("dock a="      , dock[3]) # 格式為float，地圖座標，單位為rad (deg*PI/180)
        print("dock floor="  , dock[4]) # 格式為str
        print("==========")

            
except:                      
    print("The POST JSON format has error!")             