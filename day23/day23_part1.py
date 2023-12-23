from copy import deepcopy
import sys
sys.setrecursionlimit(10000)


data = open("day23/data23.txt").read().strip().split("\n")

visited = [[False for _ in r] for r in data]

nodesByCoords = {}


def findUpstreamSplitPoints(dist, y, x, ty=None, tx=None, origin=False):
    if origin:
        pass

    if visited[y][x] and not origin and (y, x) not in nodesByCoords:
        # This might ruin everything
        # return []
        raise Exception()
    
    visited[y][x] = True

    if ty is None:
        ty = y
    if tx is None:
        tx = x
    

    # Start node
    if y == 0 and x == 1:
        return [(dist, y, x)]
    
    upstreams = []
    cnt = 0

    # End node
    if y == len(data) - 1 and x == len(data[0]) - 2:
        upstreams = [(y - 1, x)]
        cnt = 2
    else:
        # Up
        if data[y - 1][x] in ".v":
            if (not visited[y - 1][x]) or ((y - 1, x) in nodesByCoords and not (ty == y - 1 and tx == x)):
                upstreams.append((y - 1, x))
        
        # Down
        if data[y + 1][x] in ".^":
            if (not visited[y + 1][x]) or ((y + 1, x) in nodesByCoords and not (ty == y + 1 and tx == x)):
                upstreams.append((y + 1, x))
        
        # Left
        if data[y][x - 1] in ".>":
            if (not visited[y][x - 1]) or ((y, x - 1) in nodesByCoords and not (ty == x and tx == x - 1)):
                upstreams.append((y, x - 1))
        
        # Right
        if data[y][x + 1] in ".<":
            if (not visited[y][x + 1]) or ((y, x + 1) in nodesByCoords and not (ty == x and tx == x + 1)):
                upstreams.append((y, x + 1))
        
        cnt = (data[y - 1][x] != "#") + (data[y + 1][x] != "#") + (data[y][x - 1] != "#") + (data[y][x + 1] != "#")

    # Dead end
    if cnt == 1:
        return []
    # Middle nodes
    elif cnt == 2:
        return findUpstreamSplitPoints(dist + 1, *upstreams[0], ty=ty, tx=tx)
    # Split
    elif origin:
        res = []
        for uy, ux in upstreams:
            res += findUpstreamSplitPoints(dist + 1, uy, ux, ty=ty, tx=tx)
        return res
    else:
        return [(dist, y, x)]    


class Node:
    def __init__(self, y, x):
        self.y = y
        self.x = x
    
        self.inbound = []
        self.outbound = []

        self.maxDistTo = -1

    def bfs(self, dist):
        if dist <= self.maxDistTo:
            return
        
        self.maxDistTo = dist

        for d, node in self.outbound:
            node.bfs(dist + d)


q = [(len(data) - 1,len(data[0]) - 2)]

nodesByCoords[(len(data) - 1,len(data[0]) - 2)] = Node(len(data) - 1,len(data[0]) - 2)
nodesByCoords[(len(data) - 1,len(data[0]) - 2)].visited = True

while q:
    y, x = q.pop(0)

    if (y, x) not in nodesByCoords:
        nodesByCoords[(y, x)] = Node(y, x)

    # Might need to set initial distance to 1 to avoid off-by-one
    upstreams = findUpstreamSplitPoints(0, y, x, origin=True)

    for d, uy, ux in upstreams:
        if (uy, ux) not in nodesByCoords:
            nodesByCoords[(uy, ux)] = Node(uy, ux)

        nodesByCoords[(y, x)].inbound.append((d, nodesByCoords[(uy, ux)]))
        nodesByCoords[(uy, ux)].outbound.append((d, nodesByCoords[(y, x)]))

        if not (uy == 0 and ux == 1):
            q.append((uy, ux))


nodesByCoords[(0, 1)].bfs(0)

print(nodesByCoords[(len(data) - 1,len(data[0]) - 2)].maxDistTo)