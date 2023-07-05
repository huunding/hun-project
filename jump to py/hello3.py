t1 = (1,2, 'a','b')
#  del t1[0] 이렇게 되면 리스트가 아니라 튜플이 되기 때문에 값을 바꾸는 것이 불가능 print 로 보는 것은 가능
#딕셔너리 자료형 API 에 자주 활용됨 리스트에 순서가 아닌 키와 밸류를 넣어 사용
dic = {'name' : 'Eric' , 'age' :15}
print(dic['name'])
a = {1 :'a'}
a['nam'] = "익명"
print (a)
del a[1]
print(a)

b = {1:'a',2:'a'}
print(b)

c= {1:'파랑구름', 2:'이현준', 3:"민준"}
print(c.keys())
print(c.values())
print(c.items())
for k in c.keys():
    print(k)
for v in c.values():
    print(v)
for j in c.items():
    print(j)
for l,p in c.items():
    print("키는:"+ str(l))
    print("밸류는:"+p)

c.clear()
print(c.get(4,'없음')) #4만 넣으면 none 이라고 뜸
print(4 in c)

s1 = set([1,2,3])
s1 = {1,2,3}
print(type(s1))
o = [1,2,2,3,3]
newList = list(set(o))
print(newList)

result = 0
i = 1
while i<= 1000:
    if i % 3 == 0:
        result += i
    i += 1
print(result)
treeHit = 0
while treeHit < 10:
    treeHit = treeHit+1
    print("나무를 %d 번 찍었습니다." %treeHit)
    if treeHit == 10:
        print("나무 넘어갑니다.")
