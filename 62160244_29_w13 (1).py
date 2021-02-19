print("=====================>ข้อที่1.1<====================")
import networkx as nx
import matplotlib.pyplot as plt

G=nx.Graph()
G.add_nodes_from(['a', 'b', 'c','d'])
G.add_edges_from([('a', 'b'), ('b', 'c'),('b','d'),('d','c')])
print(G.degree())
nx.draw(G, with_labels=True)
plt.show()

print("====================>ข้อที่1.2<====================")
A=nx.Graph()
A.add_nodes_from(['a', 'b', 'c','d','e','f'])
A.add_edges_from([('a', 'b'), ('a','e'),('a','d'),('b','c'),('e','c'),('e','f'),('d','e'),('f','c')])
print(A.degree( ))
nx.draw(A, with_labels=True)
plt.show()

print("====================>ข้อที่1.3<====================")
B=nx.Graph()
B.add_nodes_from(['a', 'b', 'c','d','e'])
B.add_edges_from([('a','b'),('a','e'),('b','c'),('b','e'),('d','c'),('d','e')])
print(B.degree())
nx.draw(B, with_labels=True)
plt.show()

print("=====================>ข้อที่2<=====================")
C = nx.DiGraph()
C.add_nodes_from(['a', 'b', 'c','d','e','f'])
C.add_edges_from([('a', 'b'),('b','c'),('c','d'),('d','e'),('e','f'),('f','a'),('f','b'),('c','e')])


nx.draw(C, with_labels=True)
plt.show()
print("====================>ข้อที่2.1<====================")
print('SKIP')
print("====================>ข้อที่2.2<====================")
print('In-degree', C.in_degree())
print('Out-degree', C.out_degree())
sum_degree_in = 0
sum_degree_out = 0

for n in C :
    sum_degree_in = sum_degree_in + C.in_degree(n)
    sum_degree_out = sum_degree_out + C.out_degree(n)
print('Sum of in-degree =',sum_degree_in)
print('Sum of out-degree =',sum_degree_out)
print('Edge =',sum_degree_in)

print("======================>ข้อที่3<======================")
D = nx.Graph()
D.add_nodes_from(['a','b','c','d','e','f','g','h'])
D.add_edges_from([('a','b'),('a','c'),('a','d'),('b','e'),('c','e'),('d','f'),('e','h'),('e','g'),('f','g')])

array_l = nx.adjacency_matrix(D)
i = 0

print(' ', end='')
for n in D:
    print(n, end=' ')

print()
for n in D:
    print(n, array_l[i].todense())
    i +=1
print("======================>ข้อที่4.1<======================")
E=nx.Graph()
E.add_nodes_from(['a', 'b', 'c','d','e'])
E.add_edges_from([('a','b'),('a','e'),('b','c'),('e','d'),('c','d')])
print(E.degree())
nx.draw(E, with_labels=True)
plt.show()
print("======================>ข้อที่4.2<======================")
F= nx.complete_graph(['a', 'b', 'c','d','e','f'])
print(F.degree())
nx.draw(F, with_labels=True)
plt.show()
print("======================>ข้อที่4.3<======================")
H=nx.complete_bipartite_graph(('a', 'b', 'c','d'),('E', 'F', 'G'))
print(H.degree())
nx.draw(H, with_labels=True)
plt.show()