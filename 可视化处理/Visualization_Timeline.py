from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
import json
import os
def color(num,standard):
    if num==0:
        return 'w'
    elif num>=standard:
        return 'r'
    else:
        return 'b'
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.set_xlabel('user')
ax.set_ylabel('date')
ax.set_zlabel("num")

with open('Timeline.json','r') as f:
    json_data=json.load(f)

type=['查找算法','排序算法','树结构','数字操作','数组','图结构','线性表','字符串']
standard=[15,8,10,25,30,7,20,12]

chart=int(input('输入类型号：'))-1
index = 0
for stu in json_data:
    index=index+1
    x=index
    for day in range(0,45):
        y=day
        count=0
        for case in stu['timeline']:
            if case['case_day']==day:
                if case['case_type']==type[chart]:
                    count=count+1
            elif case['case_day']>day:
                break
        z=count
        point=(x,y,z)
        print(point)
        ax.bar3d(x,y,0,1,1,z, color=color(z,standard[chart]),shade=True)
plt.show()
