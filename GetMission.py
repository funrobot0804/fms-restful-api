import requests
import json
import sys

import zlib
import numpy as np
from base64 import b64encode

import time
import threading
import random

url = "http://127.0.0.1:6600"+"/get_mission"
payload = {
            "category":"all",   # "unfinish" - 回傳 '進行中' 或 '預備中' 的 task
                                # "finish"   - 回傳 '已完成' 或 '未完成但被推到紀錄區' 的 task
                                # "all"      - 回傳 '全部' 的 task
                                    
            "task_id": -1       # -1         - 回傳全部
                                # 0,1,2,3... - 回傳指定id的task           
            
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
        
        'value':{'unfinish':         # 有'unfinish'和'finish'兩種字串，端看當時POST的'category' 
                 [
                    ['3',  '2/2', 'Simulator_104', '1592209639', '60 sec', '[15938,1592209639]', '[-1,-1.0]', '0', '[0 0 0]', "[[-19.1, 28.48, -3.14, '1F'], [-5.04, 3.66, -0.0, '1F']]", 'none', "1F","50","3","1"],
                    ['5', '-1/2', 'Simulator_104', '1592209639', '60 sec', '[15938,1592209639]', '[-1,-1.0]', '0', '[0 0 0]', "[[-19.1, 28.48, -3.14, '1F'], [-5.04, 3.66, -0.0, '1F']]", 'none', "2F","40","4","-1"]
                 ] 
                }
        }
        
        
    task error會回傳以下可能字串:
        "none" => '等待執行'或'執行中'，並未有錯誤發生
        "script error" => 傳到AGV上的task python腳本發生錯誤，發生的原因: 1. AGV上的python安裝有問題、
                                                                          2. AI報錯導致腳本出錯
        "ai error" => 發生的原因: 1.可能有人透過另一個console來操作機器人
                                  2.AGV被插上Joystick，搶走控制權

        "no error" => '正常結束'，過程中沒有出任何錯誤
        "busy error" => 機器正在忙，無法執行此任務
        "already error" => 之前的錯誤尚未解除，不能執行此任務 (除非POST至'http://127.0.0.1:6600/recover_error'以解除錯誤)
        "lowbattery error" => 電量不足，不能執行此任務

    task的回傳list各欄位索引說明:
        [0]  mission index    - 任務編號 (str)
        [1]  task step        - 當前執行步驟/總步驟數 (str)
        [2]  AGV name         - 被指派的AGV名稱 (str)
        [3]  start time       - 任務開始時間 UTC timestamp (str)
        [4]  using time       - 任務使用時間 (str)
        [5]  booking id&time  - [下命令者userid, 下命令時間] (str)
        [6]  cancel id&time   - [取消者userid, 取消時間] (str)
        [7]  AGV type         - AGV類型 (str)
        [8]  AGV mode         - AGV模式 [上UV燈,下UV燈,吸塵器] (str)
        [9]  task array       - 任務指令陣列 (str)
        [10] mission error    - 錯誤訊息 (str)
        [11] start floor      - 任務起始樓層 (str)
        [12] work time        - 任務已執行時間(秒) (str)
        [13] work distance    - 任務已行走距離 (str)
        [14] group            - 任務群組編號，-1表示不屬於任何群組 (str)
    '''
    
    result = json_data['result']
    print("result=", result)
    print("----------")
    
    print("unfinish ==> ")
    print("----------")
    if 'unfinish' in json_data['value']:
        unfinish_mission_list = json_data['value']['unfinish']
        for mission in unfinish_mission_list:
            print("mission index="     , mission[0]) # 格式為字串(str)
            print("task step="         , mission[1]) # 格式為字串(str)
            print("AGV name="          , mission[2]) # 格式為字串(str)
            print("start time="        , mission[3]) # 格式為字串(str)
            print("using time="        , mission[4]) # 格式為字串(str)
            print("booking id & time=" , mission[5]) # 格式為字串(str)
            print("cancel id & time="  , mission[6]) # 格式為字串(str)
            print("AGV type="          , mission[7]) # 格式為字串(str)
            print("AGV mode="          , mission[8]) # 格式為字串(str)
            print("task array="        , mission[9]) # 格式為字串(str)
            print("mission error="     , mission[10])# 格式為字串(str)
            print("start floor="       , mission[11])# 格式為字串(str)
            print("work time="         , mission[12])# 格式為字串(str)
            print("work distance="     , mission[13])# 格式為字串(str)
            print("group="             , mission[14])# 格式為字串(str)，任務群組編號，-1表示不屬於任何群組
            print("==========")

    print("finish ==> ")
    print("----------")
    if 'finish' in json_data['value']:
        finish_mission_list = json_data['value']['finish']
        for mission in finish_mission_list:
            print("mission index="     , mission[0]) # 格式為字串(str)
            print("task step="         , mission[1]) # 格式為字串(str)
            print("AGV name="          , mission[2]) # 格式為字串(str)
            print("start time="        , mission[3]) # 格式為字串(str)
            print("using time="        , mission[4]) # 格式為字串(str)
            print("booking id & time=" , mission[5]) # 格式為字串(str)
            print("cancel id & time="  , mission[6]) # 格式為字串(str)
            print("AGV type="          , mission[7]) # 格式為字串(str)
            print("AGV mode="          , mission[8]) # 格式為字串(str)
            print("task array="        , mission[9]) # 格式為字串(str)
            print("mission error="     , mission[10])# 格式為字串(str)
            print("start floor="       , mission[11])# 格式為字串(str)
            print("work time="         , mission[12])# 格式為字串(str)
            print("work distance="     , mission[13])# 格式為字串(str)
            print("group="             , mission[14])# 格式為字串(str)，任務群組編號，-1表示不屬於任何群組
            print("==========")
            
except:                      
    print("The POST JSON format has error!")                      