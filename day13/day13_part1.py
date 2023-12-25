data = open("day13/data13.txt").read().strip().split("\n\n")

def test_column_mirror(matrix, idx):
    # Size to the left of the split
    l = idx
    # Size to the right
    r = len(matrix[0]) - idx

    for row in matrix:
        for i in range(min(l, r)):
            if row[idx + i] != row[idx - 1 - i]:
                return False
            
    return True

def test_row_mirror(matrix, idx):
    # Size above the split
    a = idx
    # Size below
    b = len(matrix) - idx

    for i in range(min(a, b)):
        if matrix[idx + i] != matrix[idx - 1 - i]:
                return False
            
    return True

matrices = [m.split("\n") for m in data]

sumColCnt = 0

for matrix in matrices:
    for i in range(1, len(matrix[0])):
        if test_column_mirror(matrix, i):
            sumColCnt += i

    for i in range(1, len(matrix)):
        if test_row_mirror(matrix, i):
            sumColCnt += i * 100

print(sumColCnt)