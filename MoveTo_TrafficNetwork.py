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

            "robot_name": "msi_sim1",            # 格式為str，指定機器的名字，如果有指定就只會挑選特定名稱的機器
                                                  
            # MoveTo_TrafficNetwork指令格式
            #
            # AMR會優先使用指定的眾多鐵軌來當作移動的依據，並指定前往目的地，使用'目的地名稱'
            # 
            # ["MoveTo_TrafficNetwork", [<目的地名稱>,<目的地所在樓層>],<行走方式>]
            # ["MoveTo_TrafficNetwork", [<目的地名稱>,<目的地所在樓層>]]
            #
            # <行走方式> : 可填可不填，
            #              "Path": 使用FollowPath的行走方式 (主動繞開障礙物)
            #              "Rail": 使用FollowRail的行走方式 (等待障礙物消失)
            #

            "task_arr":[ 
                            ["MoveTo_TrafficNetwork",["origin","sharp_city@1F"]],
                            ["MoveTo_TrafficNetwork",["origin","sharp_city@1F"], "Path"],
                            ["MoveTo_TrafficNetwork",["origin","sharp_city@1F"], "Rail"]
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