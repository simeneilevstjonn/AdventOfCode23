import networkx as n
G=n.Graph()
for r in open("d"):
 s,D=r.split(": ")
 for d in D.split():G.add_edge(s,d)
G.remove_edges_from(n.minimum_edge_cut(G))
a,b=map(len,n.connected_components(G))
print(a*b)