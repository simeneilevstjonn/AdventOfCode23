data = open("day14/data14.txt").read().strip().split("\n")

cols = [[] for _ in range(len(data[0]))]

for i in range(len(data[0])):
    for r in data:
        cols[i].append(r[i])

sumwghts = 0

for col in cols:
    nextPos = 0
    for i, x in enumerate(col):
        if x == "#": 
            nextPos = i + 1
        elif x == "O":
            # col[i] = "."
            # col[nextPos] = "#"
            sumwghts += len(col) - nextPos
            nextPos += 1

print(sumwghts)