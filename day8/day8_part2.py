instructions, data = open("day8/data8.txt").read().strip().split("\n\n")

nodes = {}

for line in data.split("\n"):
    n = line[:3]
    l = line[7:10]
    r = line[12:15]
    
    nodes[n] = {"R": r, "L": l}

c = 0
a = [i for i in nodes.keys() if i[2] == "A"]

def isFinished(a):
    for i in a:
        if i[2] != "Z":
            return False
    return True

while not isFinished(a):
    for i, x in enumerate(a):
        a[i] = nodes[x][instructions[c % len(instructions)]]
    c += 1

print(c)
