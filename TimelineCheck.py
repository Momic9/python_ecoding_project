import json
#返回两个时间相差的秒数
def cmp(t1,t2):
    start=list(map(int,t1.split('.')))
    end=list(map(int,t2.split('.')))
    return (end[0]-start[0])*3600+(end[1]-start[1])*60+(end[2]-start[2])

result=[]
with open('Timeline.json','r') as f:
    data=json.load(f)

for user in data:
    user_id=user['user_id']
    for i in range(len(user['timeline'])-1):
        record=user['timeline'][i]
        next_record=user['timeline'][i+1]
        #设置标准
        standard={'数组':120,'数字操作':180,'查找算法':180,'排序算法':180,
                  '线性表':300,'字符串':300,'树结构':600,'图结构':600}
        if record['case_day']==next_record['case_day']:
            time=cmp(record['case_time'],next_record['case_time'])
            if time<standard[record['case_type']]:
                result.append({'user_id':user_id,'code_url':record['code_url']})

f=open('检查结果/Answer_TimelineCheck.json','w')
f.write(json.dumps(result, indent=4, separators=(',', ': '),ensure_ascii=False,))
f.close()
print("OVER")
