import sys

def coinChange(n, p):
    
    mem = [0] + [sys.maxsize]*n
    
    for i in range(1, n + 1):
        for c in p:
            if c > i:
                break
            mem[i] = min(mem[i], mem[i - c] + 1)
        
    if mem[n] == sys.maxsize:
        return -1
        
    return mem[n]


print(coinChange(29, [1, 3, 5]))
print(coinChange(1, [2, 3, 5]))
print(coinChange(56, [15, 4, 3]))