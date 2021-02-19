L=int(input("Enter Lower = "))
U=int(input("Enter Upper = "))
A=set()
for x in range(L,U) :
    if x%2==0:
        A.add(x)
print('A = ',A)
B=set()
for x in range (L,U):
    if x%5 ==0:
        B.add(x)
print("B =",B)
C=set()
for x in range (L,U):
    if x%10 ==0:
        C.add(x)
print("C =",C)
print('A=',A)
print('B=',B)
print('C=',C)
print('1.1 = ',(A.union(B)).intersection(C))
print(len(A.union(B).intersection(C)))
print((B.difference(C)))
print(A.intersection(A.symmetric_difference(B)))
print("=====================================")
print("1.2 = ",(B^A).union(C))
print("=====================================")
if B.issuperset(C):
    print("1.3 = B is a superset of C")
else:
    print("1.3 = B is not a superset of C")
print("=====================================")
if C.issubset(A):
    print("1.4 = C is a proper subset of A")
else:
    print("1.4 = C is not a proper subset of A")
print("=====================================")
if B.isdisjoint(C):
    print("1.5 = B and C are disjoint")
else:
    print("1.5 = B and C are not disjoint")
print("=====================================")
import itertools
BC = set(itertools.product(B,C))
CB = set(itertools.product(C,B))
if BC==CB:
    print("1.6 = B x C is equal to C x B")
else:
    print("1.6 = B x C is not equal to C x B")
print("=====================================")
A=set()
for i in range (0,5) :
    i=int(input("Enter number of set A : "))
    A.add(i)
print(A)
B=set()
for U in range (0,5) :
    U=int(input("Enter number of set B : "))
    B.add(U)
print("A intersect B =",A.intersection(B))
print("A union B =",A.union(B))
print("A-(A sym.diff B) =",(A.symmetric_difference(B)).difference(A))
print("(B-A) union(B intersect A) =",(B.difference(A).union(B.intersection(A))))
from matplotlib_venn import venn2
from matplotlib import pyplot as plt
A=set([1,2])
B=set([2,3])
venn2(subsets=(A,B))
plt.show()
print("=====================================")
from matplotlib_venn import venn3
from matplotlib import pyplot as plt
A=set([1,2,4,5])
B=set([3,2,5,6])
C=set([4,5,6,7])
venn3(subsets=(A,B,C))
plt.show()