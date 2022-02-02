def lcs(s1, s2):

    #F(i, j): the longest common subsequence if we were to stop at indices i and j in strings s1 and s2 respectively
    #F(i, 0) = F(0, j) = 0

    mem = [[0]*(len(s2) + 1) for _ in range(len(s1) + 1)]
    
    #F(i, j) = 1 + F(i - 1, j - 1) if s1[i] = s2[j] else max(F(i - 1, j), F(j, i - 1))
    for i in range(0, len(s1)):
        for j in range(0, len(s2)):
            if s1[i] == s2[j]:
                mem[i + 1][j + 1] = 1 + mem[i][j]
            else:
                mem[i + 1][j + 1] = max(mem[i][j + 1], mem[i + 1][j])
                
    #Ans is at F(len(s1), len(s2))
    return mem[-1][-1]
    
print(lcs('ace', 'arc'))
print(lcs('ace', 'abcde'))
print(lcs('arc', 'arc'))
print(lcs('arc', 'flop'))