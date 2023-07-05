import pickle

# 딕셔너리 오브젝트
obj = {'my': 'dictionary'}  

# obj를 filename.pickle 파일에 저장
with open('filename.pickle', 'wb') as f:
    pickle.dump(obj, f)

# filename.pickle에 있는 오브젝트를 읽어옴 
with open('filename.pickle', 'rb') as f:
    obj = pickle.load(f)

print(obj)