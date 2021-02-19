print("=====================No.1=====================")
K = 0
N1 = 4
N2 = 2
N3 = 3
for i1 in range(0,N1,1):
    for i2 in range(0,N2,1):
        for i3 in range(0,N3,1):
            K = K+1
print("มีวิธีทั้งหมด",K,"ว ิธี")
print("====================No.2.1====================")
import math
import itertools
a=int(math.factorial(4)/math.factorial(2))
Cord = list(itertools.permutations([3,4,5,6],2))
print("มีทั้งหมด",a,"เลข")
print(Cord)
print("====================No.2.2====================")
import itertools
B = set(range(3,7))
C = set(range(3,7))
A = set(itertools.product(B,C))
print("มีทั้งหมด",len(A),"เลข")
print(A)
print("=====================No.3=====================")
import math
A6 = math.floor(325/6)
A17 = math.floor(325/17)
A102 = math.floor(325/102)
N_1_325 = A6+A17-A102

B6 = math.floor(103/6)
B17 = math.floor(103/17)
B102 = math.floor(103/102)
N_1_100 = B6+B17-B102

N_103_325 = N_1_325-N_1_100
print(N_103_325)
print("=====================No.4=====================")
from itertools import product
A={'0','1'}
B=list(product(A,repeat=4))
print('มีจำนวนบิตสตริงทั้งหมด',len(B),'จำนวน')
print([''.join(i) for i in B])
print("=====================No.5=====================")
import math
import itertools
a=int(math.factorial(4)/math.factorial(2))
Cord = list(itertools.permutations(['A','B','C','D'],2))
print("มีทั้งหมด",a,"วิธี")
print(Cord)
print("=====================No.6=====================")
import math
import itertools
a=int(math.factorial(5)/(math.factorial(3)*math.factorial(2)))
print("มีทั้งหมด",a,"วิธี")
print("=====================No.7=====================")
import math
import itertools
choice = math.factorial(6)/(math.factorial(2)*math.factorial(4))
number = [ '3', '4','5']
card = ['โพธิ์แดง','ข้ําวหลํามตัด']
all_card = list(itertools.product(number,card))
all_card_join=[''.join(i) for i in all_card]
card_Com = list(itertools.combinations(all_card_join, 2))
print('มีวิธีเลือกไพ่ ทั้งหมด ' , len(card_Com),'วิธี')
print(card_Com)
print("=====================No.8=====================")
from itertools import permutations
c=list(permutations('MMMMMMWWW', 4))
print([''.join(i) for i in c])
print('มีจ ํานวนวิธีทั้งหมด', len(c),'วิธี')