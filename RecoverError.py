import requests
import json
import sys

import zlib
import numpy as np
from base64 import b64encode

import time
import threading
import random

#透過此API，可將機器的錯誤狀態復原，(假設機器被修好...)

for i in range(1):        
    #print("start_time=", time.strftime("%a %b %d %H:%M:%S %Y", time.localtime(time.time()+(i*60)) ) )
    url = "http://127.0.0.1:6600"+"/recover_error"
    payload = { 
                "robot_name":"msi_beta",
                }
    r = requests.post(url, data=json.dumps(payload))   
    time.sleep(2.0)  