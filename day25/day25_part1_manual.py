import networkx as nx
import matplotlib.pyplot as plt

data = open("day25/data25.txt").read().strip().split("\n")

sources = []
dests = []

blist = [sorted(a) for a in [["rrz", "pzq"], ["ddj", "znv"], ["jtr", "mtq"]]]

for row in data:
    s, d = row.split(": ")

    for dest in d.split():
        if sorted([s, dest]) in blist:
            continue


        sources.append(s)
        dests.append(dest)

# print("sources = [", ",".join([f'"{src}"' for src in sources]), "];")
# print("dests = [", ",".join([f'"{dest}"' for dest in dests]), "];")
        
G = nx.Graph()

G.add_edges_from(zip(sources, dests))

# nx.draw_networkx(G)
# plt.show()

subgraphs = list(nx.connected_components(G))
print(len(subgraphs[0]) * len(subgraphs[1]))