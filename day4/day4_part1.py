data = open("day4/data4.txt").read().strip().split("\n")

p = 0

for line in data:
    win, yours = line.split(": ")[1].split(" | ")
    win = [int(i) for i in win.split()]
    yours = [int(i) for i in yours.split()]

    num = sum(i in win for i in yours)

    if num > 0:
        p += (1 << (num -1))

print(p)