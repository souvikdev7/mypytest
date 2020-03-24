'''
class Tree:
    wheels = 4
    def __init__(self, name):
        self.name = name
    def show(self):
        print("Hello ",self.name)

    @classmethod
    def showInfo(cls):
         return cls.wheels

    @staticmethod
    def showData():
        print("Hello we are inside static method")



#obj = Tree("Souvik")
#obj.show()
#Tree.wheels =5

#print(Tree.showInfo())
Tree.showData()



##############  Single / Multilevel Inheritance #####################
class A:
    def f1(self):
        print("in f1")

    def f2(self):
        print("in f2")


class B(A):
    def f3(self):
        print("in f3")

    def f4(self):
        print("in f4")

class C(B):
    def f5(self):
        print("in f5")

obj1 = A()
#obj1.f1()
#obj1.f2()

objB = B()
#objB.f3()
#objB.f4()
#objB.f1()
#objB.f2()
objC = C()
objC.f2()
objC.f5()

##############  Single / Multilevel   Inheritance #####################

##############  Multiple Inheritance #####################
class A:
    def f1(self):
        print("in f1")
    def f2(self):
        print("in f2")
class B:
    def f3(self):
        print("in f3")
    def f4(self):
        print("in f4")
class C(A,B):
    def f5(self):
        print("in f5")

obj1 = A()
obj1.f2()

objB = B()
objB.f3()

objC = C()
objC.f4()
objC.f1()
objC.f5()


##############  Multiple Inheritance #####################

##############  Abstruct class #####################
from abc import ABC, abstractmethod

class P(ABC) :
    @abstractmethod
    def f1(self):
       pass
    def f2(self):
        pass
    def f3(self):
        print("inside abstract class")
class M(P):
    def f1(self):
        print("in box")
    def f2(self):
        print("in bottle")


obj = M()
obj.f1()
obj.f2()
obj.f3()
##############  Abstruct class #####################

############## Multi threading  #####################
from time import sleep
from threading import *

class hello(Thread):
    def run(self):
        for i in range(5):
            print("Hello")
            sleep(1)

class hi(Thread):
    def run(self):
        for i in range(5):
            print("Hi")
            sleep(1)

t1 = hello()
t2 = hi()

t1.start()
sleep(1)
t2.start()

t1.join()
t2.join()
print("Bye")
############## Multi threading  #####################



##############   #####################


'''


##############  File Handling  #####################

from time import sleep

#ff1 = open("docs/ab1.txt","r")
#print(ff1.readlines())

path = "docs/xyz1.txt"
#ff2 = open(path,"a")
#ff2.write("\njanta carfew")
#sleep(5)
ff3 = open(path,"r")
print(ff3.read())
print("bye")



##############  File Handling  #####################






