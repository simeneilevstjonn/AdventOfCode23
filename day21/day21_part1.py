data = open("day21/data21.txt").read().strip().split("\n")

dists = [[2147483647 for _ in row] for row in data]
vis = [[False for _ in row] for row in data]

sy = -1
sx = -1

for i, row in enumerate(data):
    for j, v in enumerate(row):
        if v == "S":
            sy = i
            sx = j
            break

dists[sy][sx] = 0

q = [[sy, sx]]

def inRange(y, x):
    return 0 <= y < len(data) and 0 <= x < len(data[0]) and not vis[y][x]

while q:
    y, x = q.pop(0)
    d = dists[y][x]

    if vis[y][x] or data[y][x] == "#":
        continue

    vis[y][x] = True
 
    if inRange(y - 1, x):
        dists[y - 1][x] = d + 1
        q.append((y - 1, x))

    if inRange(y + 1, x):
        dists[y + 1][x] = d + 1
        q.append((y + 1, x))

    if inRange(y, x - 1):
        dists[y][x - 1] = d + 1
        q.append((y, x - 1))

    if inRange(y, x + 1):
        dists[y][x + 1] = d + 1
        q.append((y, x + 1))

cnt = 0
for rdi, rda in zip(dists, data):
    for d, da in zip(rdi, rda):
        cnt += d <= 64 and (d % 2 == 0) and da != "#"

print(cnt)