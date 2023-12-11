import itertools

data = open("day11/data11.txt").read().strip().split("\n")

procdata = []

for row in data:
    procdata.append(row)
    if row == "." * len(row):
        procdata.append(row)

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

for i in range(len(procdata)):
    for c in noGalaxyCols:
        procdata[i] = procdata[i][:c] + "." + procdata[i][c:]

galaxies = []

for y, row in enumerate(procdata):
    for x, val in enumerate(row):
        if val == "#":
            galaxies.append((y, x))

sumdist = 0

for a, b in itertools.combinations(galaxies, 2):
    ay, ax = a
    by, bx = b

    sumdist += abs(ay - by) + abs(ax - bx)

print(sumdist)