import requests
import json

url = "http://127.0.0.1:6600" + "/check_on_point"
payload = {
            "robot_name": "msi_default",   # AMR 名稱

            "name": "dock_0",              # 點位名稱（Target 或 Dock 的名稱）

            "type": "dock",                # "target" - 目標點位
                                           # "dock"   - 充電站

            "range": 0.2,                  # 判斷距離閾值，單位：公尺(m)
                                           # 參考點與點位的直線距離 <= range 時回傳 True

            "offset": -0.4                 # 可選，預設 0.0
                                           # 將計算用的參考點沿 AMR 的正面方向（X 軸）偏移
                                           # 單位：公尺(m)
                                           # 正值 → 往 AMR 前方移動
                                           # 負值 → 往 AMR 後方移動
                                           # 範例：offset = status.center2front
                                           #        → 參考點移至 AMR 前端中心
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
        'result': 'success',   # 'success' 代表console端沒錯誤，'fail' 代表console端可能有錯誤
                               # 'fail' 時 'value' 為錯誤訊息字串：
                               #   'robot not found' - 找不到指定的 AMR
                               #   'point not found' - 找不到指定的點位名稱

        'value': True          # True  - 參考點在點位的指定範圍內（且同一樓層）
                               # False - 參考點不在點位的指定範圍內，或不同樓層
                               # 參考點 = AMR 中心點 + offset 沿 AMR 正面方向偏移
    }
    '''

    result = json_data['result']
    print("result=", result)
    print("----------")

    if result == 'success':
        on_point = json_data['value']
        print("on_point=", on_point)   # True 或 False
    else:
        error_msg = json_data['value']
        print("error=", error_msg)

except:
    print("The POST JSON format has error!")
