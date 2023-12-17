from queue import PriorityQueue
from enum import Enum

data = [[int(i) for i in row] for row in open("day17/data17.txt").read().strip().split("\n")]

class Direction(Enum):
    Left = 0
    Right = 1
    Up = 2
    Down = 3

def djikstra():
    visited = [[[False] * 12 for _ in range(len(data[0]))] for _ in data] 
    pq = PriorityQueue()
    
    pq.put((0, 0, 0, None, 0))

    while not pq.empty():
        dist, y, x, dv, dircnt = pq.get()
        direction = Direction(dv or 0)

        if visited[y][x][direction.value + (dircnt - 1) * 4]: continue

        if dv is not None: 
            visited[y][x][direction.value + (dircnt - 1) * 4] = True

        if y == len(data) - 1 and x == len(data[0]) - 1:
            return dist
        
        # Up
        if y > 0 and not (direction == Direction.Up and dircnt == 3) and direction != Direction.Down:
            pq.put((dist + data[y - 1][x], y - 1, x, Direction.Up.value, dircnt + 1 if direction == Direction.Up else 1))
        
        # Down
        if y < len(data) - 1 and not (direction == Direction.Down and dircnt == 3) and direction != Direction.Up:
            pq.put((dist + data[y + 1][x], y + 1, x, Direction.Down.value, dircnt + 1 if direction == Direction.Down else 1))

        # Left
        if x > 0 and not (direction == Direction.Left and dircnt == 3) and direction != Direction.Right:
            pq.put((dist + data[y][x - 1], y, x - 1, Direction.Left.value, dircnt + 1 if direction == Direction.Left else 1))

        # Right
        if x < len(data[0]) - 1 and not (direction == Direction.Right and dircnt == 3) and direction != Direction.Left:
            pq.put((dist + data[y][x + 1], y, x + 1, Direction.Right.value, dircnt + 1 if direction == Direction.Right else 1))

print(djikstra())



