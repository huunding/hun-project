#구구단 만들기
#def gugu(n):
#   result = []
#    result.append(n*1)
#    result.append(n*2)
#    result.append(n*3)
#    result.append(n*4)
#    result.append(n*5)
#    result.append(n*6)
#    result.append(n*7)
#    result.append(n*8)
#    result.append(n*9)
#    return result

#print(gugu(2))

#def GuGu(n):
#    result = []
#    a = 1
#    while a <10:
#       result.append(n*i)
#        a = a + 1
#    return result
#print(GuGu(5))

#3과 5의 배수 합하기
#result = 0
#for n in range(1,1000):
#    if n % 3 == 0 or n % 5 == 0:
#        result += n
#print(result)

#게시판 페이징 하기
def getTotalPage(m,n):
    if m % n == 0:
        return m//n
    else:
        return m// n+1
print(getTotalPage(5, 10))    # 1 출력
print(getTotalPage(15, 10))   # 2 출력
print(getTotalPage(25, 10))   # 3 출력
print(getTotalPage(30, 10))   # 4 출력
