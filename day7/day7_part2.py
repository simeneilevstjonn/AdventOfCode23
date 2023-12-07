data = open("day7/exdata7.txt").read().strip().split("\n")

cardorder = "AKQT98765432J"[::-1]

class Hand:
    def __init__(self, row):
        self.hand, bid = row.split()
        self.bid = int(bid)

    def type(self):
        occ = {}

        j = 0

        for c in self.hand:
            if c == "J":
                j += 1
                continue
            if c not in occ:
                occ[c] = 1
            else:
                occ[c] += 1

        cnts = sorted(list(occ.values()))

        if not j:
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
        
        else:
            if len(occ) == 1:
                # 1, 4j or 2, 3j or 3, 2j or 4, 1j
                # Five of a kind
                return 6
            elif len(occ) == 2:
                # 1, 1, 3j or 1, 2, 2j or 2, 2, 1j
                # Four of a kind
                if j == 3 or j == 2:
                    return 5
                # Full house
                elif j == 1:
                    return 4
            elif len(occ) == 3:
                # 1, 1, 1, 2j or 1, 1, 2, 1j
                # Three of a kind
                return 3
            elif len(occ) == 4:
                # 1, 1, 1, 1, j
                # One pair
                return 1
            elif len(occ) == 0:
                # 5j
                # Five of a kind
                return 6
        
    def sortstring(self):
        handstr = [chr(0x30 + cardorder.index(x)) for x in self.hand]

        return str(self.type()) + "".join(handstr)
    
hands = [Hand(r) for r in data]
hands.sort(key = lambda x : x.sortstring())
print(*[h.hand for h in hands])


print(sum(h.bid * (i + 1) for i, h in enumerate(hands)))