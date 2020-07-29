import json
import os
import random
'''
#判断字符串集是否有规则
def is_proper(strs):
    str_recorded=[]
    count_recorded=[]
    for str in strs:
        if not (str in str_recorded):
            str_recorded.append(str)
            count_recorded.append(1)
        else:
            index=str_recorded.index(str)
            count_recorded[index]=count_recorded[index]+1
    return max(count_recorded)>=sum(count_recorded)/2
'''
#添加用例中的特殊输入输出方法
def add_exclusive_words(path,common_words):
    with open(path+'readme.md','r',encoding='UTF-8') as f:
        lines=f.readlines()
    start_record=False
    for line in lines:
        if line=="```\n":
            start_record=not start_record
        elif start_record:
            common_words.append(line.replace('\n',''))
    return common_words

#判断代码是否面向用例方法
def define_once(path,common_words):
    print(common_words)
    with open(path+'.mooctest/testCases.json', 'r',encoding='UTF-8') as f:
        output=[]
        input=[]
        json_data = json.load(f)
        for case in json_data:
            if(case['input'])!="":
                input.append(case['input'].split('\n')[int(random.random()*len(case['input'].split('\n')))])
                while input[-1]=="":
                    input.append(case['input'].split('\n')[int(random.random() * len(case['input'].split('\n')))])
                    input.remove("")
                if input[-1] in common_words:
                    input.remove(input[-1])

            if (case['output']) != "" and (case['output']) != "\n":
                output.append(case['output'].split('\n')[int(random.random()*len(case['output'].split('\n')))])
                while output[-1]=="":
                    output.append(case['output'].split('\n')[int(random.random() * len(case['output'].split('\n')))])
                    output.remove("")
                if output[-1] in common_words:
                    output.remove(output[-1])
    with open(path+'main.py','r',encoding='UTF-8') as f:
        code=str(f.read())
    print('input:')
    print(input)
    print('output:')
    print(output)
    res=-1
    #输入检测
    count=0
    for target in input:
        if(code.find(target))!=-1:
            print('hit:'+target)
            count=count+1
    if count==len(input) and count!=0:
        print("input hit")
        res=res+1
    #输出检测
    #如果输出为已经设定的字符串跳过检测
    count=0
    for target in output:
        if(code.find(target)!=-1):
            print('hit:'+target)
            count=count+1
    if count==len(output) and count!=0:
        print("output hit")
        res=res+1
    if res>=0:
        return True
    return False

def define(path):
    common_words = ['-1', '0', '1', '2', '3','4','5',
                    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                    'u', 'v', 'w', 'x', 'y', 'z',
                    'true', 'false', 'TRUE', 'FALSE', 'True', 'False',
                    'Yes', 'No', 'YES', 'NO',
                    '[]', '[', ']', 'for']
    common_words=add_exclusive_words(path,common_words)
    while(not define_once(path,common_words)):
        print('----------------------------------')
    return True
'''
os.remove('Answer.json')
f=open("Answer.json","w")
data_path="E:/数据科学大作业/test_data/"
file_list=os.listdir(data_path)
data=[]

for file in file_list:
    user_id = file
    data_path_ = data_path+user_id+"/"
    case_type_list = os.listdir(data_path_)

    print(data_path_)
    for case_type in case_type_list:
        # 每类题遍历
        case_type_path=data_path_+case_type+"/"
        case_list=os.listdir(case_type_path)
        for case in case_list:
            # 每道题遍历
            if(case.split('_')[-1]=='100') and case.split('_')[0]!='2761':
                case_id = case.split('_')[0]
                case_path=case_type_path+case+"/upload_records/"
                record_list=os.listdir(case_path)
                record=record_list[-1]
                case_path=case_path+record+'/'
                print("loading:"+case_path)
                if(define(case_path)):
                    data.append({"user_id":user_id,"code_url":case_path})
                    print('find:'+case_path)

data.sort(key=lambda x:(x["user_id"],x["code_url"]))
f.write(json.dumps(data, indent=4, separators=(',', ': '),ensure_ascii=False,))
f.close()
print("OVER")
'''
path=input("input the url:")
print("checking:")
f=open(path+'main.py','r',encoding='UTF-8')
print('path:'+path)
for code in f.readlines():
    print(code,end="")
f.close()
print("")
print(define(path))