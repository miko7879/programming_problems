def longestPalindromeSubseq(s):

    def lcs(s1, s2):
    
        #F(i, j): longest common subsequence between s1[:i] and s2[:j] 
        #F(0, j) = F(i, 0) = 0
        mem = [[0]*(len(s2) + 1) for _ in range(len(s1) + 1)]
        
        #F(i, j) = 1 + F(i - 1, j - 1) if s1[i - 1] == s2[j - 1] else max(F(i, j - 1), F(i - 1, j))
        for i in range(1, len(s1) + 1):
            for j in range(1, len(s2) + 1):
                if s1[i - 1] == s2[j - 1]:
                    mem[i][j] = mem[i - 1][j - 1] + 1
                else:
                    mem[i][j] = max(mem[i][j - 1], mem[i - 1][j])
                    
        return mem[-1][-1]
    
    
    return lcs(s, s[::-1])
    
print(longestPalindromeSubseq('bbbab'))
print(longestPalindromeSubseq('cbbd'))