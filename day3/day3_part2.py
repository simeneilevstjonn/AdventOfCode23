data = open("day3/data3.txt").read().strip().split("\n")

partnumbers = []

partnumberids = [
     [-1] * len(data[0]) for _ in range(len(data))
]

def numDiscover(lineindex, colindex, memory, acceptMemory, ids):
    global sumOfParts
    thisCol = data[lineindex][colindex]

    if lineindex != 0 and data[lineindex - 1][colindex] != '.' and not data[lineindex - 1][colindex].isnumeric():
            acceptMemory = True
    if lineindex != len(data) - 1 and data[lineindex + 1][colindex] != '.' and not data[lineindex + 1][colindex].isnumeric():
            acceptMemory = True
    
    if thisCol.isnumeric():
        memory *= 10
        memory += int(thisCol)
        ids.append(colindex)        
    
    elif thisCol == '.':
        if acceptMemory:
            partnumbers.append(memory)
            for i in ids:
                 partnumberids[lineindex][i] = len(partnumbers) - 1
        ids = []
        memory = 0
        acceptMemory = False

        if lineindex != 0 and data[lineindex - 1][colindex] != '.' and not data[lineindex - 1][colindex].isnumeric():
            acceptMemory = True
        if lineindex != len(data) - 1 and data[lineindex + 1][colindex] != '.' and not data[lineindex + 1][colindex].isnumeric():
            acceptMemory = True
    
    else:
        acceptMemory = True
        partnumbers.append(memory)
        for i in ids:
                partnumberids[lineindex][i] = len(partnumbers) - 1
        ids = []
        memory = 0
    
    if colindex != len(data[0]) - 1:
         return numDiscover(lineindex, colindex + 1, memory, acceptMemory, ids)
    else:
        if acceptMemory:
            partnumbers.append(memory)
        for i in ids:
                 partnumberids[lineindex][i] = len(partnumbers) - 1
        ids = []

for i in range(len(data)):
    numDiscover(i, 0, 0, False, [])

def discoverAdjacent(line, col):
    adj = []
    if line != 0:
        adj.append((line - 1, col))
        if col != 0:
            adj.append((line - 1, col - 1))
        if col != len(data[0]) - 1:
            adj.append((line - 1, col + 1))
    if col != 0:
            adj.append((line, col - 1))
    if col != len(data[0]) - 1:
        adj.append((line, col + 1))

    if line != len(data) - 1:
        adj.append((line + 1, col))
        if col != 0:
            adj.append((line + 1, col - 1))
        if col != len(data[0]) - 1:
            adj.append((line + 1, col + 1))

    adjids = set()
    for y, x in adj:
        if partnumberids[y][x] != -1:
            adjids.add(partnumberids[y][x])

    return [partnumbers[i] for i in adjids]

ratioSum = 0

for i, row in enumerate(data):
     for j, col in enumerate(row):
        if col == '*':
            n = discoverAdjacent(i, j)
            if len(n) == 2:
                 ratioSum += n[0] * n[1]

print(ratioSum)