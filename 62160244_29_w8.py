print("===================================================================================================")
def divided_set(d):
    S=set()
    for num in range(1,25+1):
            if(num%d)==0:
                S.add(num)
    return S
A=divided_set(2)
b=divided_set(3)
c=divided_set(5)
d=divided_set(7)

a=divided_set(1)

print("A =",A)
print("B =",b)
print("C =",c)
print("D =",d)

print("(A union B)intersection C =",a.union(b).intersection(c))
print("(A union D)XOR C =",a.union(d).symmetric_difference(c))
print("(C intersection B)union(D difference A) =",c.intersection(b).union(d.difference(a)))
print("===================================================================================================")

def f(x):
    return (x-3)**2
x=9
print(f(x))
print("===================================================================================================")

import math
def g(x):
    x = x/5
    x=math.floor(x)
    x=int(input("Enter number of X :"))
    return x
print("X =",x)
print("===================================================================================================")

def gfx(x):
    x = int(input("Enter number of X :"))
    x=g(f(x))
    return x
def fgx(x):
    x = int(input("Enter number of X :"))
    x=f(g(x))
    return x
print("g(f(x)) =",gfx(x))
print("f(g(x)) =",fgx(x))
print("===================================================================================================")

def fgfx(x):
    x = int(input("Enter number of X :"))
    x = f(g(f(x)))
    return x
def gfgx(x):
    x = int(input("Enter number of X :"))
    x = g(f(g(x)))
    return x
print("f(g(f(x)) =",f(g(f(x))))
print("g(f(g(x)) =",g(f(g(x))))
print("===================================================================================================")