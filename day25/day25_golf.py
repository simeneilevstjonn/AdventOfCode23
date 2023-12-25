import networkx as nx
G=nx.Graph()
for row in open("day25/data25.txt").readlines():
 s,d=row.split(": ")
 for dest in d.split():
  G.add_edge(s,dest)
for u,v in nx.minimum_edge_cut(G):
 G.remove_edge(u,v)
a=1
for s in nx.connected_components(G):
 a*=len(s)
print(a)