data = open("day6/data6.txt").read().strip().split("\n")

times = map(int, data[0].split(":")[1].split())
distances = map(int, data[1].split(":")[1].split())

ans = 1

for time, dist in zip(times, distances):
    wtw = 0
    for v in range(time):
        if v * (time - v)> dist:
            wtw += 1
    

    ans *= wtw

print(ans)