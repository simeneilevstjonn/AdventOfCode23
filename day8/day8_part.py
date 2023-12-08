instructions, data = open("day8/data8.txt").read().strip().split("\n\n")

nodes = {}

for line in data.split("\n"):
    n = line[:3]
    l = line[7:10]
    r = line[12:15]
    
    nodes[n] = {"R": r, "L": l}

c = 0
a = "AAA"
while a != "ZZZ":
    a = nodes[a][instructions[c % len(instructions)]]
    c += 1

print(c)
