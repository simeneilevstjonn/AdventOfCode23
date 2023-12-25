import networkx as n
G=n.Graph()
for row in open("d"):
 s,d=row.split(": ")
 for dest in d.split():
  G.add_edge(s,dest)
for u,v in n.minimum_edge_cut(G):
 G.remove_edge(u,v)
a=1
for s in n.connected_components(G):
 a*=len(s)
print(a)