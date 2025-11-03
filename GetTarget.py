import requests
import json
import sys

import zlib
import numpy as np
from base64 import b64encode

import time
import threading
import random

url = "http://127.0.0.1:6600"+"/get_target"
payload = {
            "option":"all",   # "name" - 回傳 '給定名稱' 的目的地狀態
                              # "all"  - 回傳 '全部' 的目的地狀態                       
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
        
        'value':{'target':         
                 [
                    [["N435-2",-4.82,23.44,1.58,"1F"],
                     ["N435-1",2.68,23.66,1.6,"1F"],
                     ["N100",-19.08,28.7,-3.14,"1F"],
                     ["N610",-22.24,20.48,0.0,"1F"],
                     ["N300",-10.12,16.84,1.53,"1F"]
                     ] 
                 ] 
                }
        }        
    '''
    
    result = json_data['result']
    print("result=", result)
    print("----------")
    
    print("target ==> ")
    print("----------")
 
    target_list = json_data['value']['target']
    for target in target_list:
        print("target name="   , target[0]) # 格式為字串(str)
        print("target x="      , target[1]) # 格式為float，地圖座標，單位為m
        print("target y="      , target[2]) # 格式為float，地圖座標，單位為m
        print("target a="      , target[3]) # 格式為float，地圖座標，單位為rad (deg*PI/180)
        print("target floor="  , target[4]) # 格式為str
        print("==========")

            
except:                      
    print("The POST JSON format has error!")             