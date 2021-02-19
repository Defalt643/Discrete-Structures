print("=========================")
myset = set()
X = int(input("Enter number :"))
for i in range (1,X+1) :
    myset.add(i)
print(myset)

myset = set()
X = int(input("Enter number :"))
for i in range (1,X+1) :
    myset.add(i)
print(myset)
print("=========================")
myset = set()
X = int(input("Enter number :"))
for i in range (2,X*2+1,2) :
    myset.add(i)
print(myset)
print(len(myset))
print("=========================")

S =set()
for x in range(1,21):
    if x%5==0:
        S.add(x)
print(S)
print("=========================")
S = set()
L = int(input("Enter lower bound :"))
U = int(input("Enter upper bound :"))
for i in range(L,U):
    if i%2!=0:
        S.add(i)
print(S)
print(len(S))
print("=========================")


S.remove(min(S))
S.remove(max(S))
print(S)
print(len(S))
print("=========================")

