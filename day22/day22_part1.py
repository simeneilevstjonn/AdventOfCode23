from enum import Enum

data = open("day22/data22.txt").read().strip().split("\n")

class BrickType(Enum):
    Cube = 0
    Column = 1
    RowX = 2
    RowY = 3

# z, y, x. 331 x 10 x 10
grid = [[[None] * 10 for _ in range(10)] for _ in range(331)]

class Brick:
    def __init__(self, line):
        self.ax, self.ay, self.az, self.bx, self.by, self.bz = map(int, line.replace("~", ",").split(","))

        # Single cube
        if self.ax == self.bx and self.ay == self.by and self.az == self.bz:
            self.type = BrickType.Cube
        # Column
        elif self.ax == self.bx and self.ay == self.by and self.az != self.bz: 
            self.type = BrickType.Column
        # Row x
        elif self.ax != self.bx and self.ay == self.by and self.az == self.bz: 
            self.type = BrickType.RowX
        # Row Y
        elif self.ax == self.bx and self.ay != self.by and self.az == self.bz: 
            self.type = BrickType.RowY
        # Diagonal
        else:
            raise Exception("Diagonal not implemented")
        
    def bottomNodes(self):
        if self.type == BrickType.Cube:
            return [(self.az, self.ay, self.ax)]
        elif self.type == BrickType.Column:
            if self.az < self.bz:
                return [(self.az, self.ay, self.ax)]
            else:
                return [(self.bz, self.by, self.bx)]
        elif self.type == BrickType.RowX:
            return [(self.az, self.ay, x) for x in range(min(self.ax, self.bx), max(self.ax, self.bx) + 1)]
        elif self.type == BrickType.RowY:
            return [(self.az, y, self.ax) for y in range(min(self.ay, self.by), max(self.ay, self.by) + 1)]

    def isSupported(self, notby=None):
        for z, y, x in self.bottomNodes():
            if z == 0:
                return True
            elif grid[z - 1][y][x] is not None and grid[z - 1][y][x] != notby:
                return True
        return False
    
    def allNodes(self):
        if self.type == BrickType.Cube:
            return [(self.az, self.ay, self.ax)]
        elif self.type == BrickType.Column:
            return [(z, self.ay, self.ax) for z in range(min(self.az, self.bz), max(self.az, self.bz) + 1)]
        elif self.type == BrickType.RowX:
            return [(self.az, self.ay, x) for x in range(min(self.ax, self.bx), max(self.ax, self.bx) + 1)]
        elif self.type == BrickType.RowY:
            return [(self.az, y, self.ax) for y in range(min(self.ay, self.by), max(self.ay, self.by) + 1)]
        
    def commit(self):
        for z, y, x in self.allNodes():
            grid[z][y][x] = self

    def land(self):
        while not self.isSupported():
            self.az -= 1
            self.bz -= 1
        self.commit()

    def topNodes(self):
        if self.type == BrickType.Cube:
            return [(self.az, self.ay, self.ax)]
        elif self.type == BrickType.Column:
            if self.az > self.bz:
                return [(self.az, self.ay, self.ax)]
            else:
                return [(self.bz, self.by, self.bx)]
        elif self.type == BrickType.RowX:
            return [(self.az, self.ay, x) for x in range(min(self.ax, self.bx), max(self.ax, self.bx) + 1)]
        elif self.type == BrickType.RowY:
            return [(self.az, y, self.ax) for y in range(min(self.ay, self.by), max(self.ay, self.by) + 1)]

    def wouldBreakSupportIfDisintegrated(self):
        for z, y, x in self.topNodes():
            if grid[z + 1][y][x] is not None and not grid[z + 1][y][x].isSupported(notby=self):
                return True
            
        return False

bricks = [Brick(line) for line in data]
bricks.sort(key = lambda x : min(x.az, x.bz))

for brick in bricks:
    brick.land()

print(sum(not brick.wouldBreakSupportIfDisintegrated() for brick in bricks))