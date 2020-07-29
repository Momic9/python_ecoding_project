import json
import os
os.remove("Timeline.json")
f=open("Timeline.json","w")
data_path="E:/数据科学大作业/test_data/"
file_list=os.listdir(data_path)
data=[]
for file in file_list:
    user_id = file
    timeline=[]
    time_value=0
    total_num=0
    data_path_ = data_path+user_id+"/"
    case_type_list = os.listdir(data_path_)

    print(data_path_)
    for case_type in case_type_list:
        # 每类题遍历
        case_type_path=data_path_+case_type+"/"
        case_list=os.listdir(case_type_path)
        for case in case_list:
            # 每道题遍历
            if(case.split('_')[-1]=='100'):
                case_id = case.split('_')[0]
                case_path=case_type_path+case+"/upload_records/"
                record_list=os.listdir(case_path)
                record=record_list[-1]
                time=record.split(' ')[1]
                date=(record.split(' ')[0]).split('-');
                day=0
                if(date[1]=='03'):
                    day=14+int(date[2])
                else:
                    day=int(date[2])-14
            #   if(day<0):
            #       error=2/0
                timeline.append(
                    {"case_type":case_type,
                     "case_id":case_id,
                     "case_day":day,
                     "case_time":time,
                     "code_url":case_path+record+"/"
                     }

                )
                total_num=total_num+1
                time_value=time_value+day
    #按照时间排序
    timeline.sort(key= lambda x:(x["case_day"],x["case_time"]))
    user={"user_id":user_id,"total_num":total_num,"time_value":time_value,"timeline":timeline}
    data.append(user)
data.sort(key=lambda x:(x["total_num"],x["time_value"]))
f.write(json.dumps(data, indent=4, separators=(',', ': '),ensure_ascii=False,))
f.close()









