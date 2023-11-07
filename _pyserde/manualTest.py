import json
import os 

import pyserde_core as core

with open('/home/pi/projects/pyserde/_pyserde/testres/testjson_3.json', "r", encoding='utf-8-sig') as data_file:
    data = json.load(data_file)

code = core.dict_to_code(data,
    '/home/pi/projects/pyserde/_pyserde/testres/testout_test.py')

from testres.testout_test import *

root = L_0.from_dict(data)
data_b = root.to_dict()

assert(data == data_b)


