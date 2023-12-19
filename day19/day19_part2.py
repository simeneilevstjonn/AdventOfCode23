wfs, prts = open("day19/data19.txt").read().strip().split("\n\n")


workflows = {}


def countInRange(minx, maxx, minm, maxm, mina, maxa, mins, maxs):
    if minx > maxx or minm > maxm or mina > maxa or mins > maxs:
        return 0
    
    return (maxx - minx + 1) * (maxm - minm + 1) * (maxa - mina + 1) * (maxs - mins + 1) 

class Workflow:
    def __init__(self, rules):
        self.rules = []

        for rule in rules[:-1]:
            if ":" in rule:
                condition, result = rule.split(":")
                self.rules.append((condition, result))

        self.fallback = rules[-1]

    def countconsistent(self, minx, maxx, minm, maxm, mina, maxa, mins, maxs):
        if minx > maxx or minm > maxm or mina > maxa or mins > maxs:
            return 0
        
        count = 0

        for condition, result in self.rules:
            # Values matching condition
            Minx, Maxx, Minm, Maxm, Mina, Maxa, Mins, Maxs = minx, maxx, minm, maxm, mina, maxa, mins, maxs

            if "<" in condition:
                var, val = condition.split("<")
                # exec(f"Max{var} = min(Max{var}, {int(val) - 1})")
                # exec(f"min{var} = max(min{var}, {val})")
                if var == "x":
                    Maxx = min(Maxx, int(val) - 1)
                    minx = max(minx, int(val))
                elif var == "m":
                    Maxm = min(Maxm, int(val) - 1)
                    minm = max(minm, int(val))
                elif var == "a":
                    Maxa = min(Maxa, int(val) - 1)
                    mina = max(mina, int(val))
                elif var == "s":
                    Maxs = min(Maxs, int(val) - 1)
                    mins = max(mins, int(val))

            elif ">" in condition:
                var, val = condition.split(">")
                # exec(f"Min{var} = max(Min{var}, {int(val) + 1})")
                # exec(f"max{var} = min(max{var}, {val})")

                if var == "x":
                    Minx = max(Minx, int(val) + 1)
                    maxx = min(maxx, int(val))
                elif var == "m":
                    Minm = max(Minm, int(val) + 1)
                    maxm = min(maxm, int(val))
                elif var == "a":
                    Mina = max(Mina, int(val) + 1)
                    maxa = min(maxa, int(val))
                elif var == "s":
                    Mins = max(Mins, int(val) + 1)
                    maxs = min(maxs, int(val))

            if result == "A":
                count += countInRange(Minx, Maxx, Minm, Maxm, Mina, Maxa, Mins, Maxs)
            
            elif result != "R":
                count += workflows[result].countconsistent(Minx, Maxx, Minm, Maxm, Mina, Maxa, Mins, Maxs)

        # Fallback condition
        if self.fallback == "A":
            count += countInRange(minx, maxx, minm, maxm, mina, maxa, mins, maxs)
        elif self.fallback != "R":
            count += workflows[self.fallback].countconsistent(minx, maxx, minm, maxm, mina, maxa, mins, maxs)



        return count




                
for wf in wfs.split("\n"):
    name, rule = wf.split("{")

    ruleTexts = rule[:-1].split(",")
    
    workflows[name] = Workflow(ruleTexts)

print(workflows["in"].countconsistent(1, 4000, 1, 4000, 1, 4000, 1, 4000))