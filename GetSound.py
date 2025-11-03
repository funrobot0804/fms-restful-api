import requests
import json
import sys

import zlib
import numpy as np
from base64 import b64encode

import time
import threading

# 取得規劃路線
url = "http://127.0.0.1:6600"+"/get_sound"
payload = {
            "robot_name": "msi_7"
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
                                 
      
    'value': [
                'auto_load_map_fail.mp3', 
                'auto_load_map_start.mp3', 
                'auto_load_map_stop.mp3', 
                'auto_load_map_success.mp3', 
                'load_fail.mp3', 
                'load_success.mp3', 
                'no_charging.mp3', 
                'no_set_init_map.mp3', 
                'no_set_init_pos.mp3', 
                'program_error.mp3', 
                'relocate_fail.mp3', 
                'relocate_sucess.mp3', 
                '[take_elevator]enter.mp3', 
                '[take_elevator]finish.mp3', 
                '[take_elevator]leave.mp3', 
                '[take_elevator]ready.mp3', 
                '[take_elevator]wait.mp3', 
             ]    
             
             
             # 一般會回傳 ['檔名1.mp3','檔名2.mp3','檔名3.mp3'...] (list)
             #
             #
             # 發生錯誤，回傳空的list, []                 
    }                            
    
             
'''

json_data = r.json()
print("json_data['value']=")
print(json_data['value'])