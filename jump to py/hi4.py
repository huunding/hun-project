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
say_myself("성시훈",25) #순서에 맞춰서 작성

for i in range(0,11):
    i= i + 1
    print("나무를 %d번 찍었습니다." %i)
    if i == 10:
        print("나무가 쓰러집니다.")
        break