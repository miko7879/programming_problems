def coinChangeUnique(n, p):
    
    mem = [[1]*(n + 1)] + [[1] + [0]*n for _ in range(len(p) - 1)]
    
    for max_coin_i in range(1, len(p)):
        for i in range(1, n + 1):
            for coin_i in range(0, max_coin_i + 1):
                curr_coin = p[coin_i]
                if curr_coin > i:
                    break
                mem[max_coin_i][i] += mem[coin_i][i - curr_coin] 
    
    return mem[-1][-1]
    
def coinChangeUsingExactlyT(n, p, t):
    
    mem = [[0]*(n + 1) for _ in range(t + 1)]
    mem[0][0] = 1
    
    for ti in range(1, t + 1):
        for i in range(1, n + 1):
            for c in p:
                if c > i:
                    break
                mem[ti][i] += mem[ti - 1][i - c]
    
    return mem[-1][-1]
    
def coinChangeUsingNoMoreThanT(n, p, t):
    
    mem = [[0]*(n + 1) for _ in range(t + 1)]
    mem[0][0] = 1
    
    for ti in range(1, t + 1):
        for i in range(1, n + 1):
            for c in p:
                if c > i:
                    break
                mem[ti][i] += mem[ti - 1][i - c]
    
    return sum([r[n] for r in mem])
    
def coinChangeUsingEvenNumberOfCoins(n, p, t):
    
    mem = [[0]*(n + 1) for _ in range(t + 1)]
    mem[0][0] = 1
    
    for ti in range(1, t + 1):
        for i in range(1, n + 1):
            for c in p:
                if c > i:
                    break
                mem[ti][i] += mem[ti - 1][i - c]
    
    return sum([r[n] if i % 2 == 0 else 0 for i, r in enumerate(mem)])
    

    
print(coinChangeUnique(4, [1, 2, 3, 5]))

print(coinChangeUsingExactlyT(7, [1, 2, 3, 5], 3))

print(coinChangeUsingEvenNumberOfCoins(4, [1, 3, 5, 10], 4))

print(coinChangeUsingEvenNumberOfCoins(6, [1, 3, 5, 10], 6))