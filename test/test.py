name = "시훈"
print ("내 이름은 %s 이야." %name)

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

