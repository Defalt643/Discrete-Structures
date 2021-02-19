import networkx as nx
from networkx.algorithms import bipartite as nwx
import matplotlib.pyplot as plt
print("=============================================>ข้อที่1.1<=============================================")
A = nx.Graph()
A.add_nodes_from(['a', 'b', 'c', 'd'])
A.add_edges_from([('a', 'b'),('b','c')])
A.add_edges_from([('b', 'd'), ('d', 'c')])
print(nx.is_bipartite(A))
if nx.is_bipartite(A):
    bt_node,t_node = nwx.set(A)
    print(bt_node)
    print(t_node)
nx.draw(A,with_labels=True ,node_color='orange',edge_color='blue')
print('Degree',A.degree())
plt.show()
print("=============================================>ข้อที่1.2<=============================================")
F = nx.Graph()
F.add_nodes_from(['a', 'b', 'c', 'd','e','f'])
F.add_edges_from([('a', 'b'),('b','c'),('c','f'),('f','e'),('e','d'),('d','a'),('a','e'),('e','c')])
print(nx.is_bipartite(F))
if nx.is_bipartite(F):
    bt_node,t_node = nwx.set(F)
    print(bt_node)
    print(t_node)
nx.draw(F,with_labels=True ,node_color='orange',edge_color='blue')
print('Degree',F.degree())
plt.show()
print("=============================================>ข้อที่1.3<=============================================")
F = nx.Graph()
F.add_nodes_from(['a', 'b', 'c', 'd','e','f','g','h'])
F.add_edges_from([('a', 'b'),('a','c'),('a','d'),('b','e'),('c','e'),('d','f'),('e','h'),('e','g'),('f','g')])
print(nx.is_bipartite(F))
if nx.is_bipartite(F):
    bt_node,t_node = nwx.sets(F)
    print(bt_node)
    print(t_node)
nx.draw(F,with_labels=True ,node_color='orange',edge_color='blue')
print('Degree',F.degree())
plt.show()
print("=============================================>ข้อที่2.1<=============================================")
def euler_path(G):
    if not nx.is_connected(G):
        return False
    count = 0
    for node in G:
        if G.degree(node) % 2 != 0:
            count += 1
        if count is not 2:
            return False
        return True
G = nx.Graph()
G.add_nodes_from(['a', 'b', 'c', 'd'])
G.add_edges_from([('a', 'b'), ('a', 'c'),('a','d')])
G.add_edges_from([('b', 'c'), ('b', 'd')])
print(euler_path(G))
print('Degree',G.degree())
if nx.is_eulerian(G):
    print(list(nx.eulerian_circuit(G)))
nx.draw(G, with_labels=True)
plt.show()
print("=============================================>ข้อที่2.2<=============================================")
H=nx.Graph()
H.add_nodes_from(['1','2','3','4','5','6'])
H.add_edges_from([('1','2'),('1','3'),('1','4'),('1','5'),('1','6'),('2','6'),('2','3'),('3','4'),('4','5'),('5','6')])
print(nx.is_eulerian(H))
print('Degree',H.degree())
if nx.is_eulerian(H):
    print(list(nx.eulerian_circuit(H)))
nx.draw(H, with_labels=True)
plt.show()
print("=============================================>ข้อที่2.3<=============================================")
A=nx.Graph()
A.add_nodes_from(['1','2','3','4','5','6'])
A.add_edges_from([('1','2'),('1','6'),('2','6'),('2','3'),('3','4'),('4','5'),('5','2')])
print(nx.is_eulerian(A))
print('Degree',A.degree())
if nx.is_eulerian(A):
    print(list(nx.eulerian_circuit(A)))
nx.draw(A, with_labels=True)
plt.show()
print("=============================================>ข้อที่2.4<=============================================")
B=nx.Graph()
B.add_nodes_from(['1','2','3','4'])
B.add_edges_from([('1','2'),('1','3'),('1','4'),('4','3'),('2','3')])
print(nx.is_eulerian(B))
print('Degree',B.degree())
if nx.is_eulerian(B):
    print(list(nx.eulerian_circuit(B)))
nx.draw(B, with_labels=True)
plt.show()
print("=============================================>ข้อที่3.1<=============================================")
def theorem_ore (G):
    if G.number_of_nodes() < 3 :
        return -1
    n = G.number_of_nodes()
    for node_u in G:
        neighbors_u= G.neighbors(node_u)
        for node_v in G:
            if node_v not in neighbors_u and node_u is not node_v:
                degree_of_u = G.degree(node_u)
                degree_of_v = G.degree(node_v)
                if (degree_of_u+degree_of_v) < n:
                    return -1
    return 1

G = nx.Graph()
G.add_nodes_from(['a', 'b', 'c', 'd'])
G.add_edges_from([('a', 'b'), ('a', 'c')])
G.add_edges_from([ ('b', 'd')])
G.add_edges_from([('c', 'd'),('c','b')])
nx.draw(G, with_labels = True)
plt.show()
if theorem_ore (G) is 1 :
    print("True,","This graph has a Hamilton circuit.")
else:
    print("False,","Not define.")
print("=============================================>ข้อที่3.2<=============================================")
G = nx.Graph()
G.add_nodes_from(['a','b','c','d'])
G.add_edges_from([('a','b')])
G.add_edges_from([ ('b','d'),('b','c')])
G.add_edges_from([('c','d')])
nx.draw(G, with_labels = True)
plt.show()
if theorem_ore (G) is 1 :
    print("Ture,","This graph has a Hamilton circuit.")
else:
    print("False,","Not define.")
print("=============================================>ข้อที่3.3<=============================================")
G = nx.Graph()
G.add_nodes_from(['a','b','c','d','e'])
G.add_edges_from([('a','b'),('a','c'),('a','d')])
G.add_edges_from([ ('d','b'),('d','c'),('d','a'),('d','e')])
G.add_edges_from([('c','e')])
G.add_edges_from([('b','e')])
nx.draw(G, with_labels = True)
plt.show()
if theorem_ore (G) is 1 :
    print("Ture,","This graph has a Hamilton circuit.")
else:
    print("False,","Not define.")
print("==============================================>ข้อที่4<==============================================")
G = nx.Graph()
G.add_nodes_from(['a','b','c','d','e','f'])
G.add_edges_from([('a','b'),('a','c'),('a','d'),('a','f')])
G.add_edges_from([('b','c'),('b','d'),('b','e')])
G.add_edges_from([('c','d'),('c','f')])
G.add_edges_from([('d','e'),('d','f')])
nx.draw(G, with_labels = True)
plt.show()
if theorem_ore (G) is 1 :
    print("This graph is Hamilton graph.")
else:
    print("This graph isn't Hamilton graph.")
if nx.is_eulerian(G):
     print("This graph is an Euler graph")
else:
    print("This graph isn't an Euler graph")