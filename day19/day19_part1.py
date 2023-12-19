wfs, prts = open("day19/data19.txt").read().strip().split("\n\n")

workflows = {}

for wf in wfs.split("\n"):
    name, rule = wf.split("{")

    ruleTexts = rule[:-1].split(",")

    rules = []

    for rule in ruleTexts:
        if ":" in rule:
            cond, res = rule.split(":")
            rules.append((cond, res))
        else:
            rules.append(("True", rule))
    
    workflows[name] = rules

def workflowProc(wfid, x, m, a, s):
    if wfid == "A":
        # print("A")
        return True
    elif wfid == "R":
        # print("R")
        return False
    
    # print(wfid, end=" -> ")

    workflow = workflows[wfid]

    for condition, result in workflow:
        if eval(condition):
            return workflowProc(result, x, m, a, s)

acceptCount = 0

for part in prts.split("\n"):
    exec(part[1:-1].replace(",",";"))

    if workflowProc("in", x, m, a, s):
        acceptCount += x + m + a + s

print(acceptCount)