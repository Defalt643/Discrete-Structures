print("========================================================>ข้อที่1.1<========================================================")
from simplebst import Node
from simplebst.utils import insert_node
from simplebst.traversals import pre_order_nodes
from simplebst.traversals import in_order_nodes
from simplebst.traversals import post_order_nodes
T = Node(65)
for n in [65,48,29,25,80,95,30,15,44,21,9,38]:
    insert_node(T, n)

pre_order = []
for n in pre_order_nodes(T):
    pre_order.append(n.get_value())
print("Pre-order traversal :", pre_order)

in_order = []
for n in in_order_nodes(T):
    in_order.append(n.get_value())
print("In-order traversal :", in_order)

post_order = []
for n in post_order_nodes(T):
    post_order.append(n.get_value())
print("Post-order traversal :", post_order)
print("========================================================>ข้อที่1.2<========================================================")
T = Node(45)
for n in [45,22,62,18,26,34,75,12,40,30]:
    insert_node(T, n)

pre_order = []
for n in pre_order_nodes(T):
    pre_order.append(n.get_value())
print("Pre-order traversal :", pre_order)

in_order = []
for n in in_order_nodes(T):
    in_order.append(n.get_value())
print("In-order traversal :", in_order)

post_order = []
for n in post_order_nodes(T):
    post_order.append(n.get_value())
print("Post-order traversal :", post_order)
print("========================================================>ข้อที่3.1<========================================================")
T = Node(5)
for n in [5,3,1,8,7,15]:
    insert_node(T, n)

pre_order = []
for n in pre_order_nodes(T):
    pre_order.append(n.get_value())
print("Pre-order traversal :", pre_order)

in_order = []
for n in in_order_nodes(T):
    in_order.append(n.get_value())
print("In-order traversal :", in_order)

post_order = []
for n in post_order_nodes(T):
    post_order.append(n.get_value())
print("Post-order traversal :", post_order)
print("========================================================>ข้อที่3.2<========================================================")
T = Node(10)
for n in [10,4,2,1,3,5,7,11,12]:
    insert_node(T, n)

pre_order = []
for n in pre_order_nodes(T):
    pre_order.append(n.get_value())
print("Pre-order traversal :", pre_order)

in_order = []
for n in in_order_nodes(T):
    in_order.append(n.get_value())
print("In-order traversal :", in_order)

post_order = []
for n in post_order_nodes(T):
    post_order.append(n.get_value())
print("Post-order traversal :", post_order)
print("====================================================>ข้อที่4.1 และ 4.2<=====================================================")
def prefix_evaluation(s):
    s=s.split()
    n=len(s)
    stack =[]
    for i in range(n-1,-1,-1):
        if s[i].isdigit():
            stack.append(int(s[i]))
        elif s[i]=="+":
            a=stack.pop()
            b=stack.pop()
            stack.append(float(a)+ float(b))
        elif s[i]=="*":
            a = stack.pop()
            b = stack.pop()
            stack.append(float(a)* float(b))
        elif s[i]=="/":
            a = stack.pop()
            b = stack.pop()
            stack.append(float(a)/ float(b))
        elif s[i]=="-":
            a = stack.pop()
            b = stack.pop()
            stack.append(float(a)- float(b))
    return stack.pop()
s=input("Enter prefix :")
val=prefix_evaluation(s)
print ('%.4f' %val)
print("====================================================>ข้อที่4.3 และ 4.4<=====================================================")
def postfix_evaluation(s):
    s=s.split()
    n=len(s)
    stack =[]
    for i in range(n):
        if s[i].isdigit():
            stack.append(int(s[i]))
        elif s[i]=="+":
            b=stack.pop()
            a=stack.pop()
            stack.append(float(a)+float(b))
        elif s[i]=="*":
            b = stack.pop()
            a = stack.pop()
            stack.append(float(a)*float(b))
        elif s[i]=="/":
            b = stack.pop()
            a = stack.pop()
            stack.append(float(a)/float(b))
        elif s[i]=="-":
            b = stack.pop()
            a = stack.pop()
            stack.append(float(a)-float(b))
    return stack.pop()
s=input("Enter postfix :")
val=postfix_evaluation(s)
print ('%.4f' %val)
