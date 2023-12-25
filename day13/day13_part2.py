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

def find_reflection_line(matrix, ignore=None):
    for i in range(1, len(matrix[0])):
        if test_column_mirror(matrix, i):
            if ignore is None or ignore != (0, i):
                return 0, i

    for i in range(1, len(matrix)):
        if test_row_mirror(matrix, i):
            if ignore is None or ignore != (1, i):
                return 1, i
    
    return None

idx = 0

def find_different_line(matrix):
    org = find_reflection_line(matrix)
    global idx
    idx += 1

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            # Invert
            if matrix[i][j] == ".":
                matrix[i][j] = "#"
            else:
                matrix[i][j] = "."

            new = find_reflection_line(matrix, ignore=org)

            if new is not None and new != org:
                type, idx = new
                if type == 0:
                    return idx
                else:
                    return idx * 100
            
            # Revert inversion
            if matrix[i][j] == ".":
                matrix[i][j] = "#"
            else:
                matrix[i][j] = "."

    raise Exception()




matrices = [[[j for j in i] for i in m.split("\n")] for m in data]

print(sum(find_different_line(matrix) for matrix in matrices))