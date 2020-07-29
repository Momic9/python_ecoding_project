import json
import os

def count_lines(path):
    f=open(path,'rb')
    return len(f.readlines())

os.remove("CodeLines.json")
f=open("CodeLines.json","w")
data_path="E:/数据科学大作业/test_data/"
file_list=os.listdir(data_path)

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
    user_id = file
    data_path_ = data_path+user_id+"/"
    case_type_list = os.listdir(data_path_)

    print(file)
    for case_type in case_type_list:
        # 每类题遍历
        case_type_path=data_path_+case_type+"/"
        case_list=os.listdir(case_type_path)
        for case in case_list:
            # 每道题遍历
            if(case.split('_')[-1]=='100'):
                case_id = int(case.split('_')[0])
                if case_id==2761:
                    continue
                case_path=case_type_path+case+"/upload_records/"
                record_list=os.listdir(case_path)
                record=record_list[-1]
                case_path=case_path+record+'/'
                index=find(case_id,case_type)
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









