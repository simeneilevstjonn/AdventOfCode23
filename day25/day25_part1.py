import networkx as nx

data = open("day25/data25.txt").read().strip().split("\n")

sources = []
dests = []

for row in data:
    s, d = row.split(": ")

    for dest in d.split():
        sources.append(s)
        dests.append(dest)

G = nx.Graph()

G.add_edges_from(zip(sources, dests))

for u, v in nx.minimum_edge_cut(G):
    G.remove_edge(u, v)


subgraphs = list(nx.connected_components(G))
print(len(subgraphs[0]) * len(subgraphs[1]))