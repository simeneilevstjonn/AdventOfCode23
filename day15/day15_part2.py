strings = open("day15/data15.txt").read().strip().split(",")

def hash(v):
    curval = 0
    for c in v:
        curval += ord(c)
        curval *= 17
        curval %= 0x100
    return curval

def idxOf(arr, label):
    for i, val in enumerate(arr):
        if val[0] == label:
            return i
    
    return -1

boxes = [[] for _ in range(0x100)]

for s in strings:
    if s[-1] == "-":
        label = s[:-1]
        boxidx = hash(label)

        idx = idxOf(boxes[boxidx], label)
        if idx != -1:
            boxes[boxidx].pop(idx)

    else:
        label, focLength = s.split("=")
        boxidx = hash(label)

        idx = idxOf(boxes[boxidx], label)

        if idx != -1:
            boxes[boxidx][idx] = (label, int(focLength))
        else:
            boxes[boxidx].append((label, int(focLength)))

focp = 0

for i, box in enumerate(boxes):
    for j, val in enumerate(box):
        focp += (i + 1) * (j + 1) * val[1]

print(focp)

