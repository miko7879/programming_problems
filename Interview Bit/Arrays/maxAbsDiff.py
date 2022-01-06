import sys

def maxAbsDiff(A):
        
    min_adj_val = A[0] - len(A) + 1
    max_adj_val = A[0] + len(A) - 1
    best_val = -sys.maxsize

    for i in range(1, len(A)):
        n = A[i]
        adjustment = len(A) - i - 1
        best_val = max(best_val, abs(min_adj_val - n) - adjustment, abs(max_adj_val - n) - adjustment)
        min_adj_val = min(min_adj_val, n - adjustment)
        max_adj_val = max(max_adj_val, n + adjustment)

    return best_val
    
print(maxAbsDiff([1, 3, -1]))