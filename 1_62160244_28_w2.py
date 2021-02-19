#Mr.Khummeung Wattanasaroj 62160244 Group1 No.28
#1.1
n = 433
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

#1.2
n = 1071
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

#1.3
c = 36
d = 284
while d>0:
    print('c = ', c, ' d = ', ' r = ', c%d)
    c, d = d,c % d
print('gcd(c,d) = ',c)
print("=============================")

#1.4
a = 56
b = 32
x = a
y = b
while b>0 :
    print('a = ', a, ' b = ', b, ' r =', a%b)
    a, b = b, a % b
print('gcd(a,b) = ', a)
print('lcm(a,b) = ', (x*y)//a)
print("=============================")

#1.5
print('check that "A congruence B (mod m)" ')
A = 210
B = -20
m = 10
if (m > 0) :
    if ((A-B)% m) == 0 :
        print(A,' congruence ',B,'(mod ',m, ')')
else:
    print(A,' is not congruence ' , m, ')')
print("=============================")

#1.6
seed = 7
a = 2
c = 13
m = 19
num = int(input("Enter a number of random number : "))
rn = seed
for i in range(1,num+1):
    rn = ((a * rn) + c) % m
    print(rn)
print("=============================")

#2.1
print('check that "A congruence B (mod m)" ')
A = 14
B = 216
m = 10
if (m > 0) :
    if ((A-B)% m) == 0 :
        print(A,' congruence ',B,'(mod ',m, ')')
    else:
        print(A,' is not congruence ' ,B,'(mod ' ,m, ')')
print("=============================")

#2.2
print('check that "A congruence B (mod m)" ')
A = 80
B = -304
m = 12
if (m > 0) :
    if ((A-B)% m) == 0 :
        print(A,' congruence ',B,'(mod ',m, ')')
    else:
        print(A,' is not congruence ' ,B,'(mod ' ,m, ')')
print("=============================")

#2.3
n = 3071
d = 2
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
while n > 1 :
    if n % d == 0 :
        n = n/d
        print(d)
    else:
        d = d+1
print("=============================")

#2.4
n = 5537
d = 2
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
while n > 1 :
    if n % d == 0 :
        n = n/d
        print(d)
    else:
        d = d+1
print("=============================")

#2.5
n = 20445
d = 2
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
while n > 1 :
    if n % d == 0 :
        n = n/d
        print(d)
    else:
        d = d+1
print("=============================")

#2.6
c = 32
d = 728
while d>0:
    print('c = ', c, ' d = ', ' r = ', c%d)
    c, d = d,c % d
print('gcd(c,d) = ',c)
print("=============================")

#2.7
c = 616
d = 2640
while d>0:
    print('c = ', c, ' d = ', ' r = ', c%d)
    c, d = d,c % d
print('gcd(c,d) = ',c)
print("=============================")

#2.8
c = 233
d = 53
while d>0:
    print('c = ', c, ' d = ', ' r = ', c%d)
    c, d = d,c % d
print('gcd(c,d) = ',c)
print("=============================")

#2.9
a = 65
b = 58
x = a
y = b
while b>0 :
    print('a = ', a, ' b = ', b, ' r =', a%b)
    a, b = b, a % b
print('gcd(a,b) = ', a)
print('lcm(a,b) = ', (x*y)//a)
print("=============================")

#2.10
a = 210
b = 58
x = a
y = b
while b>0 :
    print('a = ', a, ' b = ', b, ' r =', a%b)
    a, b = b, a % b
print('gcd(a,b) = ', a)
print('lcm(a,b) = ', (x*y)//a)
print("=============================")

#2.11
a = 48
b = 120
x = a
y = b
while b>0 :
    print('a = ', a, ' b = ', b, ' r =', a%b)
    a, b = b, a % b
print('gcd(a,b) = ', a)
print('lcm(a,b) = ', (x*y)//a)
print("=============================")

#2.12
seed = 7
a = 10
c = 0
m = 23
num = int(input("Enter a number of random number : "))
rn = seed
for i in range(1,num+1):
    rn = ((a * rn) + c) % m
    print(rn)
print("=============================")
