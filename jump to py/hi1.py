treeHit = 0
while treeHit < 10:
    treeHit = treeHit + 1
    print("나무를 %d번 찍었습니다." %treeHit)
    if treeHit == 10:
        print("나무 넘어갑니다.")
result = 0
i = 1
while i <= 1000:
    if i % 3 == 0:
        result += i
    i += 1
print(result)
for i in range(1,101):
    print(i)
def say():
    return 'Hi'
a= say()
print(a)
def add(a,b) :
    print("%d, %d의 합은 %d 입니다"%(a,b,a+b))
add(3,4)
def say():
    print('Hi')
say()
