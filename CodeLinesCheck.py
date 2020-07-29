import json

with open("CodeLines.json") as f:
    data=json.load(f)
result=[]
for case in data:
    answer_line=case['answer_line']
    upload_records=case['upload_records']
    for record in upload_records:
        if record['code_lines']<answer_line/2:
            result.append({'user_id':record['user_id'],'code_url':record['code_url']})

result.sort(key=lambda x:(x["user_id"],x["code_url"]))
f=open('检查结果/Answer_CodeLinesCheck.json','w')
f.write(json.dumps(result, indent=4, separators=(',', ': '),ensure_ascii=False,))
f.close()
print('OVER')