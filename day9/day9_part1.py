data = open("day9/data9.txt").read().strip().split("\n")

def diffArray(arr): 
    return [arr[i] - arr[i - 1] for i in range(1, len(arr))]
    
def allZeroes(arr):
    for i in arr:
        if i != 0:
            return False
    return True

def extrapolate(arr):
    if allZeroes(arr):
        # Nextdiff
        return 0
    
    diffs = diffArray(arr)

    nextdiff = extrapolate(diffs)
    # print("Input array ", arr, "computed nextdiff", nextdiff, "cumdiff was", cumdiff, "retdiff is", arr[-1] + nextdiff)

    return arr[-1] + nextdiff

sumcumdiffs = 0
for seq in data:
    a = [int(i) for i in seq.split()]
    nextdiff = extrapolate(a)

    sumcumdiffs += nextdiff

print(sumcumdiffs)
