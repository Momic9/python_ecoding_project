from pylab import *
import matplotlib.pyplot as plt
import json
mpl.rcParams['font.sans-serif'] = ['SimHei']
mpl.rcParams['axes.unicode_minus'] = False
with open('../检查结果/Answer_ContainCheck_L2.json') as f:
    data=json.load(f)

count={'数组':0,'数字操作':0,'查找算法':0,'排序算法':0,
                  '线性表':0,'字符串':0,'树结构':0,'图结构':0}
labels = list(count)

for record in data:
    url=record['code_url']
    case_type=url.split('/')[4]
    count[case_type]=count[case_type]+1
sizes=[]
for type in labels:
    sizes.append(count[type])
print(sizes)
explode = (0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1)

plt.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
shadow=True, startangle=90)
plt.axis('equal')
plt.show()