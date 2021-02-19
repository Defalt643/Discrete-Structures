#n=int(input("Enter number of N : "))
n=433
if n > 1 :
    for i in range(2,n) :
        if (n % i ) == 0:
            print(n, "is not a prime number")
            print(i,"time", n // i, "is",n)
            break
    else:
        print(n,"is a prime number")
else:
    print(n,"is not a prime number")
print("=============================")
print()