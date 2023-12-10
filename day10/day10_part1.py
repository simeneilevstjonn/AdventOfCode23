import sys
sys.setrecursionlimit(1000000)

data = open("day10/data10.txt").read().strip().split("\n")

class Node:
    def __init__(self, y, x, type):
        self.y = y
        self.x = x
        self.type = type
        self.edges = []
        self.dist = -1
    def _addEdge(self, nodes, dy, dx):
        try:
            self.edges.append(nodes[self.y + dy][self.x + dx])
        except IndexError:
            pass
    def addEdges(self, nodes):
        if self.type == "|":
            self._addEdge(nodes, -1, 0)
            self._addEdge(nodes, 1, 0)
        elif self.type == "-":
            self._addEdge(nodes, 0, -1)
            self._addEdge(nodes, 0, 1)
        elif self.type == "L":
            self._addEdge(nodes, -1, 0)
            self._addEdge(nodes, 0, 1)
        elif self.type == "J":
            self._addEdge(nodes, -1, 0)
            self._addEdge(nodes, 0, -1)
        elif self.type == "7":
            self._addEdge(nodes, 1, 0)
            self._addEdge(nodes, 0, -1)
        elif self.type == "F":
            self._addEdge(nodes, 1, 0)
            self._addEdge(nodes, 0, 1)
        elif self.type == "S":
            if self.y > 0:
                if nodes[self.y - 1][self.x].type in ["|", "7", "F"]:
                    self._addEdge(nodes, -1, 0)
            if self.x > 0:
                if nodes[self.y][self.x - 1].type in ["-", "L", "F"]:
                    self._addEdge(nodes, 0, -1)
            if self.x < len(nodes[0]) - 1:
                if nodes[self.y][self.x + 1].type in ["-", "J", "7"]:
                    self._addEdge(nodes, 0, 1)
            if self.y < len(nodes) - 1:
                if nodes[self.y + 1][self.x].type in ["|", "J", "L"]:
                    self._addEdge(nodes, 1, 0)

    def dfs(self, dist):
        if self.dist != -1 and dist > self.dist:
            return
        self.dist = dist
        for n in self.edges:
            n.dfs(dist + 1)


nodes = [[Node(i, j, type) for j, type in enumerate(row)] for i, row in enumerate(data)]

startnode = None

for row in nodes:
    for n in row:
        n.addEdges(nodes)
        
        if n.type == "S":
            startnode = n

startnode.dfs(0)

mdist = 0

for row in nodes:
    for n in row:
        mdist = max(mdist, n.dist)


print(mdist)