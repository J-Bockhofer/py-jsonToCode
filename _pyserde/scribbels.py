import json
import os 

import pyserde_core as core

core.json_to_code('/home/pi/projects/pyserde/_pyserde/testres/testjson_1.json','/home/pi/projects/pyserde/_pyserde/testres/testout.py')

core.json_to_code('/home/pi/projects/pyserde/_pyserde/testres/itemObject.json','/home/pi/projects/pyserde/_pyserde/testres/testout2.py')



data_path = "/home/pi/projects/pyserde/_pyserde/testres/itemObject.json"
if os.path.exists(data_path):
    with open(data_path, "r", encoding='utf-8-sig') as data_file:
        data = json.load(data_file)

if(data):
    fieldnames = data.keys()



