data = open("day20/data20.txt").read().strip().split("\n")

pulseCount = [0, 0]

nodes = {}

class Node:
    def __init__(self, type, name, dests):
        self.type = type
        self.name = name
        self.dests = dests.split(", ") if dests else []
        self.pulseState = False
        self.callers = {}
    
    def getCallerState(self, caller):
        if caller not in self.callers:
            self.callers[caller] = False

        return self.callers[caller]

    def handle(self, pulse, caller):
        # print(f"{caller} - {['low', 'high'][pulse]} -> {self.name}")

        pulseCount[pulse] += 1

        if self.type == "b":
            return [(nodes[d], self.name, pulse) for d in self.dests]
            # for d in self.dests:
            #     nodes[d].handle(pulse)
        elif self.type == "&":
            self.callers[caller] = pulse

            rv = [(nodes[d], self.name, sum(self.callers.values()) != len(self.callers)) for d in self.dests]
            # for d in self.dests:
            #     return
            #     nodes[d].handle(pulse and self.pulseState)
            return rv
        elif self.type == "%" and not pulse:
            self.pulseState = not self.pulseState
            # for d in self.dests:
            #     nodes[d].handle(self.pulseState)
            return [(nodes[d], self.name, self.pulseState) for d in self.dests]
        return []


def handlepulses():
    queue = [(nodes["roadcaster"], "button", False)]

    while queue:
        active, caller, pulse = queue.pop(0)
        queue += active.handle(pulse, caller)


for row in data:
    n, dests = row.split(" -> ")
    type = n[0]
    name = n[1:]

    nodes[name] = Node(type, name, dests)

destnames = set()
for node in nodes.values():
    for d in node.dests:
        destnames.add(d)

for d in destnames:
    if d not in nodes:
        nodes[d] = Node("b", d, "")

for node in nodes.values():
    # node.dests = [i for i in node.dests if i in nodes]
    for dest in node.dests:
        nodes[dest].getCallerState(node.name)

for _ in range(1000):
    handlepulses()

    # pulseCount[0] += 1  

print(pulseCount[0] * pulseCount[1])