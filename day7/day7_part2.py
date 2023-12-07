data = open("day7/data7.txt").read().strip().split("\n")

cardorder = "AKQT98765432J"[::-1]

class Hand:
    def __init__(self, row):
        self.hand, bid = row.split()
        self.bid = int(bid)

    def _type(self, hypval):
        occ = {}

        for c in hypval:
            if c not in occ:
                occ[c] = 1
            else:
                occ[c] += 1

        cnts = sorted(list(occ.values()))

        if len(occ) == 1:
            # 5
            # Five of a kind
            return 6
        
        elif len(occ) == 2:
            # 1, 4 or 2, 3
            if cnts[1] == 4:
                # Four of a kind
                return 5
            elif cnts[0] == 2:
                # Full House
                return 4
        
        elif len(occ) == 3:
            # 1, 1, 3 or 1, 2, 2
            if cnts[2] == 3:
                # Three of a kind
                return 3
            if cnts[1] == 2 and cnts[2] == 2:
                # Two pairs
                return 2
        
        elif len(occ) == 4:
            # 1, 1, 1, 2
            # Pair
            return 1
        
        else:
            # 1, 1, 1, 1, 1
            # High card
            return 0
    
    def rangeOrSingleLetter(self, idx):
        if self.hand[idx] != "J":
            return [self.hand[idx]]
        return cardorder[1:]
        
    def type(self):
        mval = 0
        for a in self.rangeOrSingleLetter(0):
            for b in self.rangeOrSingleLetter(1):
                for c in self.rangeOrSingleLetter(2):
                    for d in self.rangeOrSingleLetter(3):
                        for e in self.rangeOrSingleLetter(4):
                            mval = max(mval, self._type("".join([a,b,c,d,e])))
        return mval


    def sortstring(self):
        handstr = [chr(0x30 + cardorder.index(x)) for x in self.hand]

        return str(self.type()) + "".join(handstr)
    
hands = [Hand(r) for r in data]
hands.sort(key = lambda x : x.sortstring())


print(sum(h.bid * (i + 1) for i, h in enumerate(hands)))