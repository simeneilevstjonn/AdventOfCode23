import networkx as n
G=n.Graph()
for r in open("d"):
 s,D=r.split(": ")
 for d in D.split():
  G.add_edge(s,d)
G.remove_edges_from(n.minimum_edge_cut(G))
a=1
for s in n.connected_components(G):
 a*=len(s)
print(a)