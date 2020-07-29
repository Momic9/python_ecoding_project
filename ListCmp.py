import os
import json
path_1=input('input the first path:')
path_2=input('input the second path:')
with open(path_1,'r') as f1:
    data_1=json.load(f1)
with open(path_2,'r') as f2:
    data_2=json.load(f2)
res_1=list(data_1)
for index in data_2:
    if index in res_1:
        res_1.remove(index)
res_2=list(data_2)
for index in data_2:
    if index in res_2:
        res_2.remove(index)
f=open('CmpRes_'+path_1+'-'+path_2,'w')
f.write(json.dumps(res_1, indent=4, separators=(',', ': '),ensure_ascii=False,))
f.close()
f=open('CmpRes_'+path_2+'-'+path_1,'w')
f.write(json.dumps(res_2, indent=4, separators=(',', ': '),ensure_ascii=False,))
f.close()