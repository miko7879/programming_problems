import sys

def minimumAbsoluteDifference(arr):
    min_diff = sys.maxsize
    prev = None
    for n in sorted(arr):
        if prev is not None:
            min_diff = min(min_diff, n - prev)
        prev = n
    return min_diff

print(minimumAbsoluteDifference([-2, 2, 4]))
print(minimumAbsoluteDifference([3, -7, 0]))
print(minimumAbsoluteDifference([-59, -36, -13, 1, -53, -92, -2, -96, -54, 75]))
print(minimumAbsoluteDifference([1, -3, 71, 68, 17]))
