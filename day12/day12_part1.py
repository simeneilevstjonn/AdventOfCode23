data = open("day12/data12.txt").read().strip().split("\n")

def valid(string, counts):
    stspl = [len(i) for i in string.split(".") if i]
    return counts == stspl

summodes = 0
for row in data:
    string, counts = row.split()

    counts = [int(i) for i in counts.split(",")]

    smut = [i for i in string]

    qmarkpos = []

    for i, x in enumerate(smut):
        if x == "?":
            qmarkpos.append(i)

    for i in range(1 << len(qmarkpos)):
        for j, idx in enumerate(qmarkpos):
            if i & (1 << j):
                smut[idx] = "#"
            else: smut[idx] = "."
        summodes += valid("".join(smut), counts)

print(summodes)