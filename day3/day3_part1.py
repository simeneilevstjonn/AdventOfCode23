data = open("day3/data3.txt").read().strip().split("\n")

sumOfParts = 0

def numDiscover(lineindex, colindex, memory, acceptMemory):
    global sumOfParts
    thisCol = data[lineindex][colindex]

    if lineindex != 0 and data[lineindex - 1][colindex] != '.' and not data[lineindex - 1][colindex].isnumeric():
            acceptMemory = True
    if lineindex != len(data) - 1 and data[lineindex + 1][colindex] != '.' and not data[lineindex + 1][colindex].isnumeric():
            acceptMemory = True
    
    if thisCol.isnumeric():
        memory *= 10
        memory += int(thisCol)        
    
    elif thisCol == '.':
        if acceptMemory:
            sumOfParts += memory
        memory = 0
        acceptMemory = False

        if lineindex != 0 and data[lineindex - 1][colindex] != '.' and not data[lineindex - 1][colindex].isnumeric():
            acceptMemory = True
        if lineindex != len(data) - 1 and data[lineindex + 1][colindex] != '.' and not data[lineindex + 1][colindex].isnumeric():
            acceptMemory = True
    
    else:
        acceptMemory = True
        sumOfParts += memory
        memory = 0
    
    if colindex != len(data[0]) - 1:
         return numDiscover(lineindex, colindex + 1, memory, acceptMemory)
    else:
         if acceptMemory:
            sumOfParts += memory

for i in range(len(data)):
    numDiscover(i, 0, 0, False)

print(sumOfParts)

