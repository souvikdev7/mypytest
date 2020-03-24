'''
x= 5
y=9
z=x+y
print(z)

x= int(input("Enter first number"))
y= int(input("Enter second number"))
z=x+y
print(z)

i=0
while i <= 4:
    print("hello",i)
    i+=1

j = [3,"abc",100,"jk"]
for i in j:
    print(i)

j = (3,"abc",100,"jk")
for i in j:
    print(i)

j = {"souvik":"samsung","pappu":"realme","mani":"apple"}
for key, value in j.items():  # <----###
    print(key,"||",value)

j = range (10,20,2)
for i in j:
    print(i)

j = range (20,10,-2)
for i in j:
    print(i)


av = 3
i=0
while i <= 6:
    if i > av:
        print("out of stock", i)
        break
    print("hello",i)
    i+=1

 j = range (7)
for i in j:
    if i==3:
        pass
        #break
        #continue
    print("hello",i)

for i in range(4):
    for j in range(4-i):
        print("* ",end="")
    print("")

num = 10
for i in range(2,int(num/2)):
   if num%i == 0:
       print("not prime")
       break
else :
    print("prime")

from array import *
arr = array('i',[7,8,90,576])
arr.append(55)
print(arr.buffer_info())
for i in arr:
    print(i)

from numpy import *

vars = array([4,5,6,88,99,55],int)
print(vars)

from numpy import *

#arr = array([1,21,5,6,7,99])
#print(arr)
#arr2 = arr.flatten()
#print(arr2)
#arr3 = arr2.reshape(3,2,2)

m = matrix('2 1 1 ; 1 1 1; 1 1 1')
#print(m)

m2 = matrix('1 1 1 ; 1 1 1; 1 1 2')
#print(m2)

m3 = m+m2
print(m3)


def greet(x):
    print("O2",id(x))
    print(x)
    #x[2] = 22
    x=5
    print("O3",id(x))
    print(x)



#lst = [6,7,8]
lst = 8
print("O1",id(lst))
greet(lst)

def sum(*x):
    c = 0
    for i in x:
        c+=i

    print(c)


sum(1,2)

a = 10
print(id(a))
def tree():
    a= 9
    x= globals()['a']
    print(id(x))
    print('IN',a)
    globals()['a'] = 15

tree()
print('OUT',a)

#######
def fact(n):
    f=1
    for i in range(1,n+1):
        f = f*i
    return f


a = fact(5)
#print(a)
########

def fact(n):
    if n== 0:
        return 1

    return n*fact(n-1)

a = fact(4)
print(a)


#######

jj = lambda a,b : a*b
r = jj(5,6)

print(r)


num = [2,5,7,8,17,6]

r = list(filter(lambda n : n%2==0,num))

print(r)

# Ternary Operator
a=9
b=5
c= "win" if a > b else "lose"
print(c)


#Decorator
def box(a,b):
    print(a/b)

def smart(func):
    def inner(a,b):
        if a < b:
            a,b =b,a
        return func(a,b)
    return inner


xyz = smart(box)
xyz(4,2)



print(__name__)

if __name__ == "__main__":
    print("souvik")




'''
#############################


x= 3
print(x)
print(id(x))























