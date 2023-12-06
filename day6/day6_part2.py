data = open("day6/data6.txt").read().strip().split("\n")

time = int("".join(data[0].split(":")[1].split()))
dist = int("".join(data[1].split(":")[1].split()))


wtw = 0
for v in range(time):
    if v * (time - v)> dist:
        wtw += 1

print(wtw)