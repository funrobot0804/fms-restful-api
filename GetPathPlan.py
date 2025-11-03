import requests
import json
import sys

import zlib
import numpy as np
from base64 import b64encode

import time
import threading

# 取得規劃路線
url = "http://127.0.0.1:6600"+"/get_pathplan"
payload = { "robot_name": "msi_7"        # 必須指定機器人的名稱
            }
r = requests.post(url, data=json.dumps(payload))

#print(r.text)

'''
回傳資料格式
{
    'result':'success',          # 會有'success'和'fail'兩字串，'success' 代表任務新增成功
                                 #                              'fail'    代表任務新增失敗
                                 # 
                                 #
                                 
    'value': [  [-1.33, 3.55], [-1.31, 3.55], [-1.30, 3.55]...]
             
             # 一般會回傳 [[x0,y0],[x1,y1],[x2,y2],[x3,y3],[x4,y4]...] (list, 單位:公尺)
             # 機器沒在動時，回傳 [] (list)
             #
             #
             # 發生錯誤，回傳字串(str)                 
             # 錯誤字串: "TaskManager not support (version<=1.0)" (派車版本不支援)
             #           "Found no robot" (找不到機器人)
    }                            
    
             
'''

json_data = r.json()
print("json_data['value']=")
print(json_data['value'])