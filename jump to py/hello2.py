a = "hobby"
print(a.count('b'))#() 안에 있는 것이 몇 개 인지 세어줌
b= "%0.4f" % 3.124123123
print(b)
print(a.find('b'))#없으면 -1 이 나오고 있으면 그 숫자의 인덱스가 출력
c = ",".join('abcd')
print (c)
d = "Life is too short"
print(d.replace("Life", "Your leg"))
print(d.split())# 아무것도 안넣으면 띄어쓰기 기준, :이나 ""를 넣으면 이것을 기준으로 나뉨
e= ["성시훈","신기쁨","곽찬호","이준형","박준하",["귀여워","사랑해"]]
print(e[0:2])
print(e[5][1])
del e[4]
f = ["루피","나미","조로","우솝","상디"]
f.append("거프")
print(f)
f.sort()
print(f)
f.reverse()
print(f)
f.insert(6,"샹크스")
print(f)
f.remove("나미")
print(f)#여러 개 있으면 가장 앞의 하나만 지워짐. for 를 이용해 다 없앨 수 있음
print(f.index("거프"))
print(f.pop())
f.extend(["흰수염,에이스"])
print(f)