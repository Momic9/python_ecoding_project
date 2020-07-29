import json
import os

def count_lines(path):
    f=open(path,'rb')
    return len(f.readlines())

#os.remove("CodeLines.json")
f=open("检查结果/ContainCheck_CodeLinesVer.json","w")
with open("检查结果/Answer_ContainCheck_L2.json") as f_2:
    file_list=json.load(f_2)

#初始化
data=[]

def find(case_id,case_type):
    index=-1
    for case in data:
        index=index+1
        if case['case_id']==case_id and case['case_type']==case_type:
            return index
    return -1

for file in file_list:
    user_id = file['user_id']
    code_url=str(file['code_url'])
    messages=code_url.split('/')
    print(messages)

    #print(file)
    case_type=messages[4]
    case=messages[5]
    case_id = int(case.split('_')[0])
    case_path=code_url
    index=find(case_id,case_type)
    record=messages[7]
    if index==-1:
        index=len(data)
        data.append({
            'case_id':case_id,
            'case_type':case_type,
            'answer_line':count_lines(case_path+'.mooctest/answer.py'),
            'answer_rank':1,
            'total_upload':0,
            'upload_records':[]
        })

    case_lines=count_lines(case_path+'main.py')
    if case_lines<data[index]["answer_line"]:
        data[index]["answer_rank"]=data[index]['answer_rank']+1
    data[index]["total_upload"]=data[index]["total_upload"]+1
    data[index]["upload_records"].append(
        {
            "user_id":user_id,
            "code_lines":case_lines,
            "time:":record,
            "code_url":case_path
        }
    )

#排序
for i in range(len(data)):
    data[i]["upload_records"].sort(key=lambda x:(x["code_lines"]))
data.sort(key=lambda x:(x["answer_rank"],x["answer_line"]))
#print(data)


f.write(json.dumps(data, indent=4, separators=(',', ': '),ensure_ascii=False,))
f.close()
print('success')









