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

def _map(value, range):
    dest, src, length = range
    if src <= value < src + length:
        return dest + value - src
        
    return value

def bigRangeToRanges(lo, length, maps):
    srcranges = [[lo, length]]
    destranges = []
    
    for dest, src, length in maps:
        nsr = []
        for l, le in srcranges:
            h = le + l
            
            if (src <= l < length + src) and (src <= h - 1 < length + src):
                destranges.append([_map(l, [dest, src, length]), le])
            elif (src <= l < length + src):
                destranges.append([_map(l, [dest, src, length]), length + src - l])
                if h - length - src > 0:
                    nsr.append([length + src, h - length - src])
            elif (src <= h < length + src):
                destranges.append([_map(src, [dest, src, length]), h - src])
                if src - l > 0:
                    nsr.append([l, src - l])

        destranges = nsr
    
    return srcranges + destranges
                
ranges = [[seeds[i], seeds[i + 1]] for i in range(0, len(seeds), 2)]

for map in maps:
    nr = []
    for lo, le in ranges:
        nr += bigRangeToRanges(lo, le, map)
    ranges = nr

m = min(ranges, key=lambda x : x[0])
print(m[0])