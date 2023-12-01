import re
data = open("day1/data1.txt").read().strip()

def valueOf(s):
    if s.isnumeric():
        return int(s)
    else: 
        return ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"].index(s)


data = data.split("\n")

s = sum(valueOf((m:=re.findall("(?=(\d|one|two|three|four|five|six|seven|eight|nine))", l))[0]) * 10 + valueOf(m[-1]) for l in data)

print(s)