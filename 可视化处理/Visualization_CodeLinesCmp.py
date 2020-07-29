import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import json

# 中文乱码和坐标轴负号处理。
matplotlib.rc('font', family='SimHei', weight='bold')

#计算异常代码平均代码行数

total_lines_a={'数组':0,'数字操作':0,'查找算法':0,'排序算法':0,
                  '线性表':0,'字符串':0,'树结构':0,'图结构':0}
nums_a={'数组':0,'数字操作':0,'查找算法':0,'排序算法':0,
                  '线性表':0,'字符串':0,'树结构':0,'图结构':0}
labels = list(nums_a)
with open('../检查结果/ContainCheck_CodeLinesVer.json') as f:
    data=json.load(f)

for case in data:
    caes_type=case['case_type']
    nums_a[case['case_type']]=nums_a[case['case_type']]+case['total_upload']
    for record in case['upload_records']:
        total_lines_a[caes_type]=total_lines_a[caes_type]+record['code_lines']

avg_a=[]
for label in labels:
    avg_a.append(total_lines_a[label]/nums_a[label])
print(avg_a)

#计算正常代码的平均代码行数
total_lines_b={'数组':0,'数字操作':0,'查找算法':0,'排序算法':0,
                  '线性表':0,'字符串':0,'树结构':0,'图结构':0}
nums_b={'数组':0,'数字操作':0,'查找算法':0,'排序算法':0,
                  '线性表':0,'字符串':0,'树结构':0,'图结构':0}
labels = list(nums_b)
with open('../CodeLines.json') as f:
    data=json.load(f)

for case in data:
    caes_type=case['case_type']
    nums_b[case['case_type']]=nums_b[case['case_type']]+case['total_upload']
    for record in case['upload_records']:
        total_lines_b[caes_type]=total_lines_b[caes_type]+record['code_lines']

avg_b=[]
for label in labels:
    avg_b.append((total_lines_b[label]-total_lines_a[label])
                 /(nums_b[label]-nums_a[label]))
print(avg_b)

#绘图
size = 8
x = np.arange(size)
a = np.random.random(size)
total_width, n = 0.8, 2
width = total_width / n

# redraw the coordinates of x

x = x - (total_width - width) / 2
# here is the offset

plt.bar(x, avg_a, width=width, label='面向用例代码')
plt.bar(x + width, avg_b, width=width, label='普通代码')
plt.xlabel('题目类型')
plt.xticks([0,1,2,3,4,5,6,7,8],labels)
plt.legend()
plt.show()