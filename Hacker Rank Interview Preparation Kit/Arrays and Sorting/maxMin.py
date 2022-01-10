import sys

def maxMin(k, arr):
    arr.sort()
    min_unfairness = sys.maxsize
    for i in range(0, len(arr) - k + 1):
        min_unfairness = min(min_unfairness, arr[i + k - 1] - arr[i])
    return min_unfairness
    
print(maxMin(2, [1, 4, 7, 2]))
print(maxMin(3, [10, 100, 300, 200, 1000, 20, 30]))
print(maxMin(4, [1, 2, 3, 4, 10, 20, 30, 40, 100, 200]))
print(maxMin(2, [1, 2, 1, 2, 1]))