from enum import Enum
import sys
sys.setrecursionlimit(10000000)

data = open("day16/data16.txt").read().strip().split("\n")

class Direction(Enum):
    Left = 0
    Right = 1
    Up = 2
    Down = 3

energised = [[False] * len(data[0]) for _ in range(len(data))]
visited = [[[False] * 4 for _ in range(len(data[0]))] for _ in range(len(data))]

def lightTrace(y, x, dir):
    if y < 0 or x < 0 or y > len(data) - 1 or x > len(data[0]) - 1:
        return

    if visited[y][x][dir.value]:
        return
    
    visited[y][x][dir.value] = True

    energised[y][x] = True

    t = data[y][x]

    if t == "/":
        if dir == Direction.Left:
            lightTrace(y + 1, x, Direction.Down)
        elif dir == Direction.Right:
            lightTrace(y - 1, x, Direction.Up)
        elif dir == Direction.Up:
            lightTrace(y, x + 1, Direction.Right)
        elif dir == Direction.Down:
            lightTrace(y, x - 1, Direction.Left)

    elif t == "\\":
        if dir == Direction.Left:
            lightTrace(y - 1, x, Direction.Up)
        elif dir == Direction.Right:
            lightTrace(y + 1, x, Direction.Down)
        elif dir == Direction.Up:
            lightTrace(y, x - 1, Direction.Left)
        elif dir == Direction.Down:
            lightTrace(y, x + 1, Direction.Right)
    
    elif t == "-" and dir in [Direction.Up, Direction.Down]:
        lightTrace(y, x + 1, Direction.Right)
        lightTrace(y, x - 1, Direction.Left)
    
    elif t == "|" and dir in [Direction.Left, Direction.Right]:
        lightTrace(y + 1, x, Direction.Down)
        lightTrace(y - 1, x, Direction.Up)

    else:
            if dir == Direction.Left:
                lightTrace(y, x - 1, dir)
            elif dir == Direction.Right:
                lightTrace(y, x + 1, dir)
            elif dir == Direction.Up:
                lightTrace(y - 1, x, dir)
            elif dir == Direction.Down:
                lightTrace(y + 1, x, dir)


lightTrace(0, 0, Direction.Right)

print(sum(sum(i) for i in energised))