import networkx as n
G=n.Graph()
[[G.add_edge(r.split()[0][:3],d)for d in r.split()[1:]]for r in open("d")]
G.remove_edges_from(n.minimum_edge_cut(G))
a,b=map(len,n.connected_components(G))
print(a*b)