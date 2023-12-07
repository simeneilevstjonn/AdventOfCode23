data = open("day7/data7.txt").read().strip().split("\n")

cardorder = "AKQJT98765432"[::-1]

class Hand:
    def __init__(self, row):
        self.hand, bid = row.split()
        self.bid = int(bid)

    def type(self):
        occ = {}

        for c in self.hand:
            if c not in occ:
                occ[c] = 1
            else:
                occ[c] += 1

        cnts = sorted(list(occ.values()))

        if len(occ) == 1:
            return 6
        
        elif len(occ) == 2:
            if cnts[1] == 4:
                return 5
            elif cnts[0] == 2:
                return 4
        
        elif len(occ) == 3:
            if cnts[2] == 3:
                return 3
            if cnts[1] == 2 and cnts[2] == 2:
                return 2
        
        elif len(occ) == 4:
            return 1
        
        else:
            return 0
        
    def sortstring(self):
        handstr = [chr(0x30 + cardorder.index(x)) for x in self.hand]

        return str(self.type()) + "".join(handstr)
    
hands = [Hand(r) for r in data]
hands.sort(key = lambda x : x.sortstring())


print(sum(h.bid * (i + 1) for i, h in enumerate(hands)))