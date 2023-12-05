data = open("day5/data5.txt").read().strip().split("\n")

seeds = [int(i) for i in data[0].split("seeds: ")[1].split()]

maps = []
cur = []

for line in data[3:]:
    if line:
        if line[0].isalpha():
            maps.append(cur)
            cur = []
        else:
            cur.append([int(i) for i in line.split()])

maps.append(cur)

def map(value, ranges):
    for dest, src, length in ranges:
        if src <= value < src + length:
            return dest + value - src
        
    return value
        
def allMaps(value):
    for m in maps:
        value = map(value, m)
    return value

print(min(allMaps(i) for i in seeds))