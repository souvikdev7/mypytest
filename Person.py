class Person:
    wheels = 4
    def __init__(self,n = "",a = 0):
        self.name = n
        self.age = a

    def getData(self):
        print("Name is {0} : Age is {1}".format(self.name,self.age))

c1 = Person("samir",2)
c2 = Person("amit",10)


c1.getData()
c2.getData()

#c1.wheels = 6
#c2.wheels = 8
Person.wheels = 2

print(c1.wheels)
print(c2.wheels)