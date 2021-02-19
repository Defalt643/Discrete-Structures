import math
print("Calculate the area of the shape \n1 Circle \n2 Triangle \n3 Rectangle")
A = int(input("Choose the shape :"))
def circle(r):
    area = math.pi*r**2
    print("Area of the circle =",area)
def triangle(h,b):
    area = (1/2)*b*h
    print("Area of the triangle =", area)
def rectangle(w,l):
    area = w*l
    print("Area of the rectangle =", area)
if A == 1 :
    r = int(input("Enter radius :"))
    circle(r)
elif A == 2 :
    b = int(input("Enter base :"))
    h = int(input("Enter height :"))
    triangle(h,b)
elif A == 3 :
    w = int(input("Enter width :"))
    l = int(input("Enter length :"))
    rectangle(w,l)
else:
    print("Please choose 1 or 2 or 3")