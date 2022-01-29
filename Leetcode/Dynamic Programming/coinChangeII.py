def numWaysChange(amount, coins):
    
    coins.sort()
    
    #F(i, j) = number of ways to make a change of size i where the last coin is j
    mem = [[0]*len(coins) for _ in range(amount + 1)]
    
    #F(0, j) = 1
    mem[0] = [1]*len(coins)
    
    #F(i, j) = F(i, j - 1) + 1(i - coins[j] >= 0)*F(i - j, j)
    
    #   1 2 5
    # 0 1 1 1
    # 1 1 1 1
    # 2 1 2 2
    # 3 1 2 2
    # 4 1 3 3
    # 5 1 3 4
    
    for a in range(1, amount + 1):
        for j in range(0, len(coins)):
            if j > 0:
                mem[a][j] += mem[a][j - 1]
            if a - coins[j] >= 0:
                mem[a][j] += mem[a - coins[j]][j]
            
    return mem[amount][-1]
    
print(numWaysChange(5, [1,2,5]))