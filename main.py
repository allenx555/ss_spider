# -*- coding: utf-8 -*-
# @Time    : 2018/3/18 0018 15:19
# @Author  : allenx555
# @FileName: main.py
# @Software: PyCharm

import json

new_path = "D://ss_spider/items.json"
old_path = "D://ss/gui-config.json"
with open(new_path, 'r') as f:
    new = json.loads(f.read())
with open(old_path, 'r') as f:
    old = json.loads(f.read())

old['configs'][1]['server'] = new['US_IP']
old['configs'][1]['server_port'] = eval(new['US_Port'].replace("\n", ""))
old['configs'][1]['password'] = new['US_PW'].replace("\n", "")
old['configs'][2]['server'] = new['JP_IP']
old['configs'][2]['server_port'] = eval(new['JP_Port'].replace("\n", ""))
old['configs'][2]['password'] = new['JP_PW'].replace("\n", "")
old['configs'][3]['server'] = new['SG_IP']
old['configs'][3]['server_port'] = eval(new['SG_Port'].replace("\n", ""))
old['configs'][3]['password'] = new['SG_PW'].replace("\n", "")

with open(old_path, 'w') as f:
    jsObj = json.dumps(old, indent=1)
    f.write(jsObj)
    f.close()
