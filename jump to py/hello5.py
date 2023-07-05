result = 0
def add(num):
    global result
    result += num
    return result
print (add(3))
print (add(4))

class Calculator:
    def __init__(self):
        self.result = 0
    def add(self, num):
        self.result += num
        return self.result
cal1 = Calculator()
cal2 = Calculator()
print(cal1.add(3))
print(cal1.add(4))
print(cal2.add(3))
print(cal2.add(7))

class FourCal:
    def setdata(self,first,second):
        self.first = first
        self.second = second
a= FourCal()
a.setdata(1,2) #a 가 위의 self 에, 1이 first에 2가 second 에 들어감
print(a.first)
print(a.second)

class FourCal:
    def setdata(self, first, second):
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result
a = FourCal()
a.setdata(4, 2)
print(a.add())

class FourCal:
    def __init__(self,first,second):#init 은 이 커맨드를 실행할 때 init을 먼저 실행하고 진행하게 하는 것
        self.first = first
        self.second = second
    def setdata(self, first, second):
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result
a = FourCal(2,4)


from mod1 import add
print(add(1,2))