import itertools

data = open("day11/data11.txt").read().strip().split("\n")

procdata = []

noGalaxyRows = []

for i, row in enumerate(data):
    procdata.append(row)
    if row == "." * len(row):
        noGalaxyRows.append(i)

noGalaxyCols = []
for i in range(len(data[0])):
    hasGalaxy = False
    for row in data:
        if row[i] == "#":
            hasGalaxy = True
            break
    if not hasGalaxy:
        noGalaxyCols.append(i)

noGalaxyCols.sort(reverse=True)

galaxies = []

for y, row in enumerate(procdata):
    for x, val in enumerate(row):
        if val == "#":
            galaxies.append((y, x))

sumdist = 0

for a, b in itertools.combinations(galaxies, 2):
    ay, ax = a
    by, bx = b

    dy = abs(ay - by)
    dx = abs(ax - bx)

    for i in range(min(ay, by), max(ay, by) + 1):
        if i in noGalaxyRows:
            dy += 999999
    for i in range(min(ax, bx), max(ax, bx) + 1):
        if i in noGalaxyCols:
            dx += 999999        

    sumdist += dy + dx

print(sumdist)