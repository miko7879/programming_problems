def numDistinct(s, t):
    
    #F(i, j): number of distinct subsequences of s[:j] that are equal to t[:i]
    mem = [[0]*(len(s) + 1) for _ in range(len(t) + 1)]
    
    #F(0, j) = 1
    for j in range(len(s) + 1):
        mem[0][j] = 1
    
    #F(i, j) = F(i, j - 1) + 1(s[j - 1] == t[i - 1])*F(i - 1, j - 1)
    for i in range(1, len(t) + 1):
        for j in range(1, len(s) + 1):
            mem[i][j] = mem[i][j - 1]
            if s[j - 1] == t[i - 1]:
                mem[i][j] += mem[i - 1][j - 1]
    
    return mem[-1][-1]
                                                 
print(numDistinct('rabbbit', 'rabbit'))
print(numDistinct('babgbag', 'bag'))


#   0 r a b b b i t
# 0 1 1 1 1 1 1 1 1
# r 0 1 1 1 1 1 1 1
# a 0 0 1 1 1 1 1 2
# b 0 0 0 1 2 3 3 3
# b 0 0 0 0 1 3 3 3
# i 0 0 0 0 0 0 3 3
# t 0 0 0 0 0 0 0 3