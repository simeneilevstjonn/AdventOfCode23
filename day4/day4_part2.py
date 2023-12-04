data = open("day4/data4.txt").read().strip().split("\n")

cardcount = [1] * len(data)

for j, line in enumerate(data):
    win, yours = line.split(": ")[1].split(" | ")
    win = [int(i) for i in win.split()]
    yours = [int(i) for i in yours.split()]

    num = sum(i in win for i in yours)

    if num > 0:
        for k in range(j + 1, min(j + 1 + num, len(data))):
            cardcount[k] += cardcount[j]


print(sum(cardcount))