import requests
import json
import sys

import zlib
import numpy as np
from base64 import b64encode

import time
import threading

# 取消指定任務
url = "http://127.0.0.1:6600"+"/cancel_mission"
payload = { "taskindex":int(5),   #格式為int，指定'想取消'的任務id
            "userid":int(15938)   #格式為int，'取消者'的使用者id
            }
r = requests.post(url, data=json.dumps(payload))