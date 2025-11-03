import requests
import json
import sys

import zlib
import numpy as np
from base64 import b64encode

import time
import threading
import random


url = "http://127.0.0.1:6600"+"/set_drone"
payload = { "act":"None",            # "None" -> 新增, 更新
                                     # "DEL" ->  將drone刪除
            "x": 0.0,              
            "y": 0.0,
            "battery": 81,
            "id": "A2"               # drone的ID, 不同的ID會再新增1個drone的物件
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
        'result':'success',          # 會有'success'和'fail'兩字串，'success' 代表任務新增成功
                                     #                              'fail'    代表任務新增失敗
                                     # 
                                     #
                                     
        'value': 3                   # 有可能是'數字'或'字串'
                                     # 數字 0,1,2,3... => 指派成功的task id
                                     # 字串 "xxxxx" => 無法指派的原因                                     
                                     #      "task array type error" => task_arr的格式有誤   
                                     #      "task array empty" => task_arr是空的
                                     #      "task start time in past" => 指派任務的時間是在"過去"
                                     #      "taskManager loop dead lock" => console的task manager當了
                                     #      "robot error" => AGV有錯誤，無法指派
                                     #      "reserver overlap" => 指派的任務時間與其他任務重疊，無法指派
                                     #      "no robot" => 無空閒的AGV在指定的時間可以指派       
            
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