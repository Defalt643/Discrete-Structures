print("=========================")
x = int(input("Enter a number : "))
for i in range(0,x,1):
    print(i)
print("=========================")
a = []
N = int(input("Enter N :"))
for i in range(N):
    X=int(input('x='))
    a.append(X)
    a.sort(reverse = True)
print("Min =",min(a))
print("Max =",max(a))
print("Average =",sum(a)/len(a))

print("=========================")
b=a.copy()
del b[0]
print(b)
print("Min =",min(b))
print("Max =",max(b))
print("Average =",sum(b)/len(b))

