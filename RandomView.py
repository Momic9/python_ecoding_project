import os
import json
import random
f=open('检查结果/Answer_ContainCheck_L2.json','r')
json_data=json.load(f)
path=json_data[int(random.random()*len(json_data))]['code_url']
f=open(path+'readme.md','r',encoding='UTF-8')
for code in f.readlines():
    print(code,end="")
f.close()
print()
print('-------------代码内容---------------')
f=open(path+'main.py','r',encoding='UTF-8')
print('path:'+path)
for code in f.readlines():
    print(code,end="")
f.close()