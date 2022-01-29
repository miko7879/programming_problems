import sys

def coinChange(coins, amount):
    
    coins.sort()
    
    #F(i): the minimum number of coins to get a change of i
    mem = [sys.maxsize]*(amount + 1)
    
    #F(0) = 0
    mem[0] = 0
    
    #F(i) = min(1(i - c >= 0)*F(i - c) for all c in coins)
    for i in range(1, amount + 1):
        for c in coins:
            if i - c < 0:
                break
            mem[i] = min(mem[i], mem[i - c] + 1)
        
    if mem[amount] == sys.maxsize:
        return -1
    
    return mem[amount]
    
print(coinChange([1, 2, 5], 11))