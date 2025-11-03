import requests
import json
import sys

import zlib
import numpy as np
from base64 import b64encode

import time
import threading
import random


url = "http://127.0.0.1:6600"+"/set_mission"
payload = { "start_time":float( time.time() ),    # 格式為float，西元1970年後所經過的浮點秒數(UTC)         
            "using_time":float(300),              # 格式為float，任務欲使用的浮點秒數
            "userid":int(15938),                  # 格式為int，下命令者的userid
            "robot_type":int(0),                  # 格式為int，欲使用的robot type (垃圾車、送餐車、送衣服車...)
            "robot_mode":[0,0,0],                 # 格式為list，0 => off
                                                  #             1 => on
                                                  # [上UV燈、下UV燈、吸塵器]
            "robot_name":"msi_sim1",             # 格式為str，指定機器的名字，如果有指定就只會挑選特定名稱的機器
                                                  
            # MissionScript指令格式
            #
            # 命令AMR使用設定好的Mission Script (會將Mission Script還原成原本的task array)
            #
            # ["MissionScript", "xxx", "EXTRA", ["-c","5"]]
            # 
            # "xxx"      -> str，指定Mission Script的名稱
            #
            # "EXTRA"    -> str，指定從哪裡取得的Mission Script
            #               "FMS": 從FMS取得，FMS會將Mission Script還原成各個Step
            #               "UPLOADED": 從上傳至AMR的一群ission Script內取得 
            #               "EXTRA": 從EXTRA的內建資料夾取得
            # 
            # ["-c","5"] -> List (Array) of str
            #               輸入的ARGV參數，如果Mission Script允許輸入ARGV參數
            
            "task_arr":[ 
                         ["MissionScript", "A12"],
                         ["MissionScript", "A123", "FMS"],
                         ["MissionScript", "B50", "UPLOADED"],
                         ["MissionScript", "LiftUp", "EXTRA"],
                         ["MissionScript", "LiftDown", "EXTRA"],
                         ["MissionScript", "LiftDown", "EXTRA", ["-c","5"]]
                       ] 
                                                                            
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