import sys
from copy import deepcopy
sys.setrecursionlimit(1000000)

data = open("day23/data23.txt").read().strip().replace("v", ".").replace("^", ".").replace("<", ".").replace(">", ".").split("\n")

nodeNextId = 0

nodesByCoords = {}

class Node:
    def __init__(self, y, x):
        self.y = y
        self.x = x
        global nodeNextId
        self.id = nodeNextId
        nodeNextId += 1

        self.edges = []
        self.dfsVisited = [[False for _ in r] for r in data]

        self.maxDistTo = -1

    def dfs(self, dist, y, x):
        assert not self.dfsVisited[y][x]
        
        self.dfsVisited[y][x] = True

        if y in [0, len(data) - 1]: 
            degree = 10000
        else:
            degree = (data[y - 1][x] != "#") + (data[y + 1][x] != "#") + (data[y][x - 1] != "#") + (data[y][x + 1] != "#")
            upstreams = []
            # Up
            if data[y - 1][x] == ".":
                if (not self.dfsVisited[y - 1][x]):
                    upstreams.append((y - 1, x))
            
            # Down
            if data[y + 1][x] == ".":
                if (not self.dfsVisited[y + 1][x]):
                    upstreams.append((y + 1, x))
            
            # Left
            if data[y][x - 1] == ".":
                if (not self.dfsVisited[y][x - 1]):
                    upstreams.append((y, x - 1))
            
            # Right
            if data[y][x + 1] == ".":
                if (not self.dfsVisited[y][x + 1]):
                    upstreams.append((y, x + 1))


        # Dead end
        if degree == 1:
            return None
        # Middle node
        elif degree == 2:
            assert len(upstreams) == 1

            return self.dfs(dist + 1, *upstreams[0])
        # Split point
        elif degree > 2:
            return (dist, y, x)
        
    def discoverAdjacentNodes(self):
        upstreams = []

        self.dfsVisited[self.y][self.x] = True

        # Start node
        if self.y == 0 and self.x == 1:
            upstreams = [(1, 1)]
        # End node
        elif self.y == len(data) - 1 and self.x == len(data[0]) - 2:
            upstreams = [(len(data) - 2, len(data[0]) - 2)]
        else:
            # Up
            if data[self.y - 1][self.x] == ".":
                if (not self.dfsVisited[self.y - 1][self.x]):
                    upstreams.append((self.y - 1, self.x))
            
            # Down
            if data[self.y + 1][self.x] == ".":
                if (not self.dfsVisited[self.y + 1][self.x]):
                    upstreams.append((self.y + 1, self.x))
            
            # Left
            if data[self.y][self.x - 1] == ".":
                if (not self.dfsVisited[self.y][self.x - 1]):
                    upstreams.append((self.y, self.x - 1))
            
            # Right
            if data[self.y][self.x + 1] == ".":
                if (not self.dfsVisited[self.y][self.x + 1]):
                    upstreams.append((self.y, self.x + 1))

        for uy, ux in upstreams:
            res = self.dfs(1, uy, ux)
            if res is not None:
                dist, y, x = res

                self.edges.append((dist, nodesByCoords[(y, x)]))

    def otherGraphDfs(self, dist, visited):
        if visited[self.id]:
            return
        
        visited[self.id] = True
        
        self.maxDistTo = max(dist, self.maxDistTo)
        
        for d, node in self.edges:
            if not visited[node.id]:
                node.otherGraphDfs(dist + d, deepcopy(visited))

for y, row in enumerate(data):
    for x, c in enumerate(row):
        if x in [0, len(data[0]) - 1]: 
            continue
        if c != "#":
            if y in [0, len(data) - 1]: 
                degree = 10000
            else:
                degree = (data[y - 1][x] != "#") + (data[y + 1][x] != "#") + (data[y][x - 1] != "#") + (data[y][x + 1] != "#")

            if degree > 2:
                nodesByCoords[(y, x)] = Node(y, x)

for node in nodesByCoords.values():
    node.discoverAdjacentNodes()

nodesByCoords[(0, 1)].otherGraphDfs(0, [False] * len(nodesByCoords))

print(nodesByCoords[(len(data) - 1,len(data[0]) - 2)].maxDistTo)