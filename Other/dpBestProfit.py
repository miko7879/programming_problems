def profitablePath(coins):
    
    #Memory array
    mem = [[-1]*len(coins[r]) for r in range(len(coins))]
    frm = [[(-1, -1)]*len(coins[r]) for r in range(len(coins))]
    
    #Edge case (0, 0)
    mem[0][0], frm[0][0] = coins[0][0], (0, 0)
    if mem[0][0] == -1:
        return -1, (-1, -1)
            
    #Edge case (0, c =/= 0)
    for c in range(1, len(coins[0])):
        if coins[0][c] == -1:
            break
        mem[0][c], frm[0][c] = mem[0][c - 1] + coins[0][c], (0, c - 1)
        
    #Edge case (r =/= 0, 0)
    for r in range(1, len(coins)):
        if coins[r][0] == -1:
            break
        mem[r][0], frm[r][0] = mem[r - 1][0] + coins[r][0], (r - 1, 0)
        
    #Solve problem bottom-up
    for r in range(1, len(coins)):
        for c in range(1, len(coins[r])):
            if coins[r][c] == -1:
                continue
            if mem[r - 1][c] > mem[r][c - 1]:
                mem[r][c], frm[r][c] = mem[r - 1][c] + coins[r][c], (r - 1, c)
            else:
                mem[r][c], frm[r][c] = mem[r][c - 1] + coins[r][c], (r, c - 1)
                
                
    #Check for unreachable solution
    if mem[-1][-1] == -1:
        return -1, (-1, -1)
    
    #Calculate the path
    path = []
    par = frm[-1][-1]
    while par != (0, 0):
        path.append(par)
        par = frm[par[0]][par[1]]
        
    path.reverse()
    
    return mem[-1][-1], [(0, 0)] + path + [(len(coins) - 1, len(coins[0]) - 1)]
    
coins = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
print(profitablePath(coins))

coins = [[1, 3, 1, 1, 2], [2, 1, 1, 1, 1], [5, 4, 4, 2, 1]]
print(profitablePath(coins))

coins = [[-1, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
print(profitablePath(coins))

coins = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, -1]]
print(profitablePath(coins))

coins = [[2, 1, -1, 10, 12], [1, 3, 4, 6, 5], [12, 1, 1, 1, 1]]
print(profitablePath(coins))

coins = [[1, 4, 12, -1, 0], [1, -1, 0, 100, 1000], [1, 1, 1, 1, 1]]
print(profitablePath(coins))