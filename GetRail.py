import requests
import json
import sys

import zlib
import numpy as np
from base64 import b64encode

import time
import threading
import random

# 根據交通管理設定，有時候派遣系統會自動計算產生軌跡，透過此API，只可將'手動規劃'的軌跡抓出來

url = "http://127.0.0.1:6600"+"/get_rail"
payload = {
            "option":"all",   # "name" - 回傳 '給定名稱' 的軌跡(鐵軌)狀態
                              # "all"  - 回傳 '全部' 的軌跡(鐵軌)狀態                       
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
        
        'value':{'rail':         
                 [
                    [
                     ["T1",[-4.74,6.48],[-10.66,21.06],507,"1F",[[-4.72,6.48],[-4.71,6.48]...]],
                     ["T2",[-22.22,20.42],[-19.58,28.58],666,"1F",[[-22.22,20.42],[-22.20,20.42]...]]
                    ] 
                 ] 
                }
        }        
    '''
    
    result = json_data['result']
    #print("result=", result)
    print("----------")
    
    print("rail ==> ")
    print("----------")
 
    rail_list = json_data['value']['rail']
    for rail in rail_list:
        print("rail name="   , rail[0]) # 格式為字串(str)
        print("rail start="  , rail[1][0], ",", rail[1][1]) # 格式為float，地圖座標，單位為m
        print("rail end="    , rail[2][0], ",", rail[2][1]) # 格式為float，地圖座標，單位為m
        print("rail length=" , rail[3]) # 格式為int
        print("rail floor="  , rail[4]) # 格式為str
        #print("rail path="   , rail[5]) # 格式為list, [[x0, y0],[x1, y1]...[x99,y99]...]
        print("==========")

            
except:                      
    print("The POST JSON format has error!")             