#파이썬 함수의 구조는 def 함수명(매개변수)  input
#                      <수항핼 문장1> 
#                      <수행할문장2>...  = function
#                      return 리턴 값   = output
def sum(a,b):
    result = a+b
    return result
print(sum(1,2))
def sum(a,b):
    print("%d, %d의 합은 %d 입니다"%(a,b,a+b))
print(sum(1,2))
myList = [1,2,3]
print(myList.pop(2)) #append 는 출력이 없는 함수, pop 은 출력값이 있음.
def sum_many(*args): #*를 붙이고 뒤에 단어를 넣으면 거기에 있는 것을 다 더함.
    sum = 0
    for i in args:
        sum = sum + i
    return sum
print(sum_many(1,2,3))

def print_kwargs(**kwargs):
    for k in kwargs.keys():
        if(k == "name"):
            print("당신의 이름은 :" + kwargs[k])
print(print_kwargs (name="int 조수", b="2"))

def sum_and_mul(a,b):
    return a+b, a*b, a-b
print (sum_and_mul(1,2))#괄호안에 [0]을 쓰면 0번째 인덱스 값만 출력

def say_myself(name, age, man=True): 
    print("나의 이름은 %s 입니다." % name) 
    print("나이는 %d살입니다." % age) 
    if man: 
        print("남자입니다.")
    else: 
        print("여자입니다.")
say_myself("성시훈",20,True) #순서에 맞춰서 작성

a= 1
def vartest(a):
    a=a+1
vartest(a)
print(a)

myList = [lambda a,b: a+b, lambda a,b: a*b]
print(myList[0](1,2))

a= input()
print(a)

print("life","is","too","short.")
for i in range(10):
    print(i, end ='hi1')

f = open("새파일.txt",'w',encoding="UTF-8")
for i in range(1,11):
    data="%d번째 줄입니다.\n" %i
    f.write(data)
f.close()

f = open("새파일.txt",'r',encoding="UTF-8")
line = f.readline()
print(line)
f.close()

f = open("새파일.txt",'r',encoding="UTF-8")
while True:
    line = f.readline()
    if not line: break
    print(line)
f.close()#한 줄 읽기

f = open ("새파일.txt",'r', encoding="UTF-8")
lines = f.readlines()
for line in lines:
    print(line, end= "")
f.close() #리스트로 읽기

f= open("새파일.txt",'r',encoding="UTF-8")
data = f.read()
print(data)
f.close()#통째로 읽기

f= open("새파일.txt",'a',encoding="UTF-8")
for i in range(11, 20):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)
f.close()

with open("foo.txt",'w') as f:
    f.write("Life is too shrot, you need python")