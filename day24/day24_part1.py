import numpy as np

data = open("day24/data24.txt").read().strip().split("\n")

INTERSECT_MIN = 200000000000000
INTERSECT_MAX = 400000000000000

# INTERSECT_MIN = 7
# INTERSECT_MAX = 27

nlid = 0

class Line:
    def __init__(self, row):
        self.rx, self.ry, self.rz, self.vx, self.vy, self.vz = map(int, row.replace("@", ",").split(","))

        global nlid
        self.id = nlid
        nlid += 1

    def intersectInXY(self, line):
        # Linear equation system
        # rx0 + vx0t = rx1 + vx1s
        # ry0 + vy0t = ry1 + vy1s


        a = np.matrix([[self.vx, -line.vx], [self.vy, -line.vy]])
        b = np.matrix([[line.rx - self.rx], [line.ry - self.ry]])


        try:
            sol = np.linalg.solve(a, b)
            t, s = sol
        except np.linalg.LinAlgError:
            return 0, 0

        y = self.ry + self.vy * float(t)
        x = self.rx + self.vx * float(t)

        if float(t) < 0 or float(s) < 0:
            return 0, 0

        return y, x
    
lines = [Line(row) for row in data]

cnt = 0
for a in lines:
    for b in lines:
        if a == b:
            continue
        
        y, x = a.intersectInXY(b)

        cnt += (INTERSECT_MIN <= y <= INTERSECT_MAX) and (INTERSECT_MIN <= x <= INTERSECT_MAX)

print(cnt // 2)