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
        
        self.onlySupportedByMemo = {}
        
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
    
    def unset(self):
        for z, y, x in self.allNodes():
            grid[z][y][x] = None

    def land(self, notby=None):
        moved = False
        while not self.isSupported(notby=notby):
            if not moved:
                self.unset()
            moved = True
            self.az -= 1
            self.bz -= 1
        
        if moved:
            self.commit()
        return moved

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
    
    def determineSupportersAndSupported(self):
        self.supports = set()
        for z, y, x in self.topNodes():
            if grid[z + 1][y][x] is not None:
                self.supports.add(grid[z + 1][y][x])
        
        self.supportedBy = set()
        for z, y, x in self.bottomNodes():
            if z == 0:
                continue
            if grid[z - 1][y][x] is not None:
                self.supportedBy.add(grid[z - 1][y][x])
    
    def onlySupportedBy(self, brick):
        if min(self.az, self.bz) == 0:
            return False
        
        if brick in self.onlySupportedByMemo:
            return self.onlySupportedByMemo[brick]

        onlySupported = True

        for node in self.supportedBy:
            if node == brick:
                continue
            onlySupported = onlySupported and node.onlySupportedBy(brick)

        self.onlySupportedByMemo[brick] = onlySupported

        return onlySupported
        

bricks = [Brick(line) for line in data]
bricks.sort(key = lambda x : min(x.az, x.bz))

for brick in bricks:
    brick.land()

bricks.sort(key = lambda x : min(x.az, x.bz))

# print(sum(not brick.wouldBreakSupportIfDisintegrated() for brick in bricks))

def deepCopyOfGrid():
    return [[row[::] for row in layer] for layer in grid]

sumFallBricks = 0

for brick in bricks:
    brick.determineSupportersAndSupported()

for brick in bricks:
    if brick.wouldBreakSupportIfDisintegrated():
        # gridBackup = deepCopyOfGrid()
        
        # for b in bricks:
        #     if b != brick:
        #         sumFallBricks += b.land(brick)

        # grid = gridBackup
        for b in bricks:
            if b != brick:
                sumFallBricks += b.onlySupportedBy(brick)

print(sumFallBricks)


