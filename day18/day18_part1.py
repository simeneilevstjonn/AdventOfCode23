import sys
sys.setrecursionlimit(1000000)

data = open("day18/data18.txt").read().strip().split("\n")

# Fixed size grid, increase if things crash
grid = [[False] * 1000 for _ in range(1000)] 
grid[500][500] = True

posy = 500
posx = 500

for row in data:
    dir, cnt, clr = row.split()

    cnt = int(cnt)

    for i in range(cnt):
        if dir == "L":
            posx -= 1
        elif dir == "R":
            posx += 1
        elif dir == "U":
            posy -= 1
        else:
            posy += 1
        
        grid[posy][posx] = True

visited = [[False] * 1000 for _ in range(1000)] 
parents = [[(i, j) for j in range(1000)] for i in range(1000)] 
shouldCount = [[False] * 1000 for _ in range(1000)] 

def uf(y, x, py, px):
    if y < 0 or x < 0 or y > 999 or x > 999:
        return True
    
    if visited[y][x]:
        return True
    
    if grid[y][x]:
        return True
    
    visited[y][x] = True
    parents[y][x] = (py, px)

    
    inside = uf(y - 1, x, py, px) 
    inside = uf(y + 1, x, py, px) and inside
    inside = uf(y, x - 1, py, px) and inside
    inside = uf(y, x + 1, py, px) and inside
    inside = inside and not (y == 0 or x == 0 or y == 999 or x == 999)

    shouldCount[y][x] = inside

    return inside

for i in range(1000):
    for j in range(1000):
        if not visited[i][j] and not grid[i][j]:
            uf(i, j, i, j)

cnt = 0

for i in range(1000):
    for j in range(1000):
        if grid[i][j]:
            cnt += 1
        else:
            py, px = parents[i][j]
            cnt += shouldCount[py][px]

print(cnt)
