import json

# 딕셔너리 오브젝트
obj = {'my': 'dictionary'}  

# obj를 filename.json 파일에 저장
with open('filename.json', 'w') as f:
    json.dump(obj, f)

# filename.json에 있는 오브젝트를 읽어옴 
with open('filename.json', 'r') as f:
    obj = json.load(f)

print(obj)