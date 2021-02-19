print("===================>ข้อที่1<===================")
from math import factorial as fac
import itertools
f = ['F']
num1 = set('123456789')
m = ['M']
num2 = set('1234')
female = list(itertools.product(f,num1))
female_join = set([''.join(i)for i in female])
male = list(itertools.product(m,num2))
male_join = set([''.join(i)for i in male])
fac1 = fac(13)/(fac(8)*fac(5))
print("Have",fac1,"Ways")
print("==================>ข้อที่1.2<==================")
X = fac(9)/(fac(5)*fac(4))
Y = fac(4)/fac(3)
fac2 = X*Y
print("Have",fac2,"Ways")
print("==================>ข้อที่1.3<==================")
x = fac(9)/(fac(4)*fac(5))
y = fac(4)/(fac(0)*fac(4))
fac3 = x*y
print("Have",fac3,"Ways")
print("==================>ข้อที่1.4<==================")
A = fac(9)/(fac(8)*fac(1))
B = fac(4)/(fac(0)*fac(4))
fac4 = A*B
print("Have",fac4,"Ways")
print("===================>ข้อที่2<===================")
from itertools import permutations
L1=list(permutations('ABCDE', 4))
l1 = [''.join(i) for i in L1]
print(l1)
print("Have",len(l1),"Ways")
print("===================>ข้อที่3<===================")
L2=list(permutations(['A','B','C','D','E'], 4))
print("Have",len(L2),"Ways")
print(L2)
print("==================>ข้อที่4.1<==================")
import math
import itertools
a = int(math.factorial(8)/math.factorial(5))
Cord = list(itertools.permutations(['EX.1','EX.2','EX.3','EX.4','EX.5','EX.6','EX.7','EX.8'],5))
print("Have",len(Cord),"Ways")
print(Cord)
print("==================>ข้อที่4.2<==================")
from itertools import product
A5={'EX.1','EX.2','EX.3','EX.4','EX.5','EX.6','EX.7','EX.8'}
C3=set(product(A5,repeat=5))
print('สามตัวมีทั้งหมด', len(C3),'จ ํานวน')
print([''.join(i) for i in C3])

print("===================>ข้อที่5<===================")
M = list(['A','B','C','D','E','F','J','K','M','N','O','P','Q','R','S'])
W = list(itertools.permutations(M,2))
print("Have",len(W),"Ways")
print(W)
print("===================>ข้อที่6<===================")
from itertools import product
A={'0','1','3','A','B'}
B3=list(product(A,repeat=3))
B4=list(product(A,repeat=4))
print('สามตัวมีทั้งหมด', len(B3),'จ ํานวน')
print([''.join(i) for i in B3])
print('สี่ตัวมีทั้งหมด', len(B4),'จ ํานวน')
print([''.join(i) for i in B4])
print("รวมทั้งหมด",len(B3)+len(B4),'จำนวน')
