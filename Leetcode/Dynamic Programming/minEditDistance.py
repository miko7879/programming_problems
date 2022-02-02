def minEditDistance(word1, word2):
    
    #F(i, j): the edit distance between word1[:i], word2[:j]
    mem = [[0]*(1 + len(word2)) for _ in range(len(word1) + 1)]
    
    #F(i, 0) = i
    for i in range(len(word1)):
        mem[i + 1][0] = i + 1
    
    #F(0, j) = j
    for j in range(len(word2)):
        mem[0][j + 1] = j + 1
    
    #F(i, j) = F(i - 1, j - 1) if word1[i - 1] == word2[j - 1]: if characters are equal nothing to do, so edit distance is same as that of the two immediately smaller substrings
    #F(i, j) = 1 + min(F(i - 1, j), F(i, j - 1), F(i - 1, j - 1)): if there is a mismatch, we must either:
    #   1) swap word1[i] to word2[j]: F(i - 1, j - 1)
    #   2) insert word2[j] into position i: F(i - 1, j)
    #   3) delete word1[i]: F(i, j - 1)
    #   Select the smallest of the above and add 1 to the operation count, build bottom - up
    for i in range(1, len(word1) + 1):
        for j in range(1, len(word2) + 1):
            if word1[i - 1] == word2[j - 1]:
                mem[i][j] = mem[i - 1][j - 1]
            else:
                mem[i][j] = 1 + min(mem[i - 1][j], mem[i][j - 1], mem[i - 1][j - 1])
    
    #Answer is at F(len(word1) + 1, len(word2) + 1)
    return mem[-1][-1]
    
print(minEditDistance('intention', 'execution'))
print(minEditDistance('ros', 'horse'))