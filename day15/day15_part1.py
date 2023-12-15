strings = open("day15/data15.txt").read().strip().split(",")

def hash(v):
    curval = 0
    for c in v:
        curval += ord(c)
        curval *= 17
        curval %= 0x100
    return curval

sumhash = sum(hash(i) for i in strings)

print(sumhash)