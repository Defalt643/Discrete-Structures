N = int(input("Enter number of input :"))
def input_data(N):
    List = []
    odd = []
    even = []
    for i in range(N):
        X = int(input('Enter a number :'))
        List.append(X)
        if X%2==0:
            odd.append(X)
        else:
            even.append(X)
    print("List A =",List)
    print("Max A =",max(List))
    print("Min A =",min(List))
    print("Average A =",sum(List)/len(List))
    print("Number of even :",len(odd))
    print("Number of odd :",len(even))
input_data(N)