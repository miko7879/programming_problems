def getMinimumCost(k, c):
    mult = 1
    friend = 0
    tot = 0
    for n in sorted(c, reverse = True):
        tot += n*mult
        friend += 1
        if friend == k:
            mult += 1
            friend = 0
    return tot
    
print(getMinimumCost(3, [1, 2, 3, 4]))
print(getMinimumCost(3, [2, 5, 6]))
print(getMinimumCost(2, [2, 5, 6]))
print(getMinimumCost(3, [1, 3, 5, 7, 9]))