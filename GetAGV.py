import requests
import json
import sys

import zlib
import numpy as np
from base64 import b64encode

import time
import threading
import random

url = "http://127.0.0.1:6600"+"/get_agv"
payload = {
            "option":"all",   # "name" - 回傳 '給定名稱' 的AGV狀態
                              # "all"  - 回傳 '全部' 的AGV狀態 
                                    
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
        
        'value':{'agv':         
                 [
                    ["Simulator_104",-19.082,28.441,-1.134,"1F",80,"running", 26, 3, 0, 3, "end,standby", 1, "172.16.114.141", 935488, 5, 0] 
                 ] 
                }
        }        
    '''
    
    result = json_data['result']
    print("result=", result)
    print("----------")
    
    print("agv ==> ")
    print("----------")
 
    agv_list = json_data['value']['agv']
    for agv in agv_list:
        print("agv name="           , agv[0])  # 格式為字串(str)
        print("agv x(unit:m)="      , agv[1])  # 格式為float
        print("agv y(unit:m)="      , agv[2])  # 格式為float
        print("agv a(unit:rad)="    , agv[3])  # 格式為float
        print("agv floor="          , agv[4])  # 格式為字串(str)
        print("agv power="          , agv[5])  # 格式為int
        print("agv task status="    , agv[6])  # 格式為字串(str), 有"standby", "running", "error"三種狀態
        print("agv volts="          , agv[7])  # 格式為int
        print("agv ai_status="      , agv[8])  # 格式為int, 詳見AI狀態代碼表
        print("agv ai_error="       , agv[9])  # 格式為int, 詳見AI狀態代碼表
        print("agv ai_info="        , agv[10]) # 格式為int, 詳見AI狀態代碼表
        print("agv ai_name="        , agv[11]) # 格式為字串(str)
        print("agv charging="       , agv[12]) # 格式為int, 0跟1, 表示是否有在充電
        print("agv ip addr="        , agv[13]) # 格式為字串(str)
        print("agv work time="      , agv[14]) # 格式為int，單位: 秒(seconds)
        print("agv work distance="  , agv[15]) # 格式為int，單位: 公尺(m)
        print("agv is UV work="     , agv[16]) # 格式為int，0跟1, 表示UVC是否有在工作
        print("==========")

            
except:                      
    print("The POST JSON format has error!")             