from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
import json
import os
def color(num,standard):
    if num==0:
        return 'w'
    elif num>=standard:
        return 'g'
    elif num/standard>0.5:
        return 'y'
    else:
        return 'r'

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.set_xlabel('case')
ax.set_ylabel('record')
ax.set_zlabel("lines")
filename=input("输入json文件名：")
with open(filename,'r') as f:
    json_data=json.load(f)

type=['查找算法','排序算法','树结构','数字操作','数组','图结构','线性表','字符串']

chart=int(input('输入类型号：'))-1
index = 0
#题目遍历
for case in json_data:
    if chart!=-1 and case['case_type']!=type[chart]:
        continue
    index=index+1
    x=index
    count=0
    #提交遍历
    for record in case['upload_records']:
        count=count+1
        y=count
        z=record['code_lines']
        point=(x,y,z)
        print(point)
        ax.bar3d(x,y,0,1,1,z, color=color(z,case['answer_line']),shade=True)
plt.show()
