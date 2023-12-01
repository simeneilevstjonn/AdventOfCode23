import re
data = open("day1/data1.txt").read().strip().split("\n")

s = sum(int((m:=re.findall("\d", l))[0] + m[-1]) for l in data)

print(s)