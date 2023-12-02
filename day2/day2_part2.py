import numpy as np

data = open("day2/data2.txt").read().strip().split("\n")

# RGB
limits = np.array([12, 13, 14])

def lineToMatrix(line):
    lines = line.split(";")
    arys = []

    for l in lines:
        lv = [0, 0, 0]
        p = l.split(",")
        for vp in p:
            num, col = vp.split()

            lv[["red", "green", "blue"].index(col)] = int(num)
        arys.append(lv)

    return np.matrix(arys)

s = sum(np.prod(np.max(lineToMatrix(l.split(": ")[1]), axis=0)) for l in data)
print(s)