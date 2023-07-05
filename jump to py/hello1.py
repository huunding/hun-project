#int 정수형 : 1,2,3
#float 실수형 : 1.1 , 1.2
a = 3
b = 4
print (a+b)
print (a*b)
print (a/b)
print (a//b)
print (a**b)
c = "Hello World"
print(type(c))
d = 'Python\'s favorite food is perl'
print (d)
e = 'Life is too short \n You need python'
print(e)
f = """Hi my name is sihun!
nice to meet you."""
print(f)
print(e[0:4:2])
#이상:미만:간격
number = 10
day = "three"
g = "I eat %d apples. so I was sick for %s days." %(number, day) # %d : 정수 %f: 실수 %s: 스트링
print(g)

h = "I'm {age} years old. And my Name is {name}".format(name="sihun", age = "25")
print (h)

name = "int"
j = f"나의 이름은 {name}입니다" 
print (j)