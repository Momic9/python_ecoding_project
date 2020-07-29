import matplotlib
import matplotlib.pyplot as plt
import json

# 中文乱码和坐标轴负号处理。
matplotlib.rc('font', family='SimHei', weight='bold')
plt.rcParams['axes.unicode_minus'] = False

#计算分子
numerate=[]
with open('../检查结果/Answer_ContainCheck_L2.json') as f:
    data=json.load(f)

count={'数组':0,'数字操作':0,'查找算法':0,'排序算法':0,
                  '线性表':0,'字符串':0,'树结构':0,'图结构':0}
labels = list(count)

for record in data:
    url=record['code_url']
    case_type=url.split('/')[4]
    count[case_type]=count[case_type]+1
for type in labels:
    numerate.append(count[type])

#计算分母
denominator=[]
count={'数组':0,'数字操作':0,'查找算法':0,'排序算法':0,
                  '线性表':0,'字符串':0,'树结构':0,'图结构':0}
with open('../CodeLines.json') as f:
    data=json.load(f)
for case in data:
    count[case['case_type']]=count[case['case_type']]+case['total_upload']
for type in labels:
    denominator.append(count[type])

result=[]
for i in range(len(labels)):
    result.append(numerate[i]/denominator[i]*100)

# 绘图。
fig, ax = plt.subplots()
b = ax.barh(range(len(labels)), result, color='#6699CC')

# 为横向水平的柱图右侧添加数据标签。
for rect in b:
    w = rect.get_width()
    ax.text(w, rect.get_y() + rect.get_height() / 2, '%d' %
            w+'%', ha='left', va='center')

# 设置Y轴纵坐标上的刻度线标签。
ax.set_yticks(range(len(labels)))
ax.set_yticklabels(labels)

# 不要X横坐标上的label标签。
plt.xticks(())

plt.show()