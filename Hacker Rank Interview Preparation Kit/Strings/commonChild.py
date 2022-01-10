def commonChild(s1, s2):
    
    lcs = [[0]*(len(s1) + 1) for _ in range(len(s2) + 1)]
    
    for s2i in range(1, len(s2) + 1):
        for s1i in range(1, len(s1) + 1):
            if s1[s1i - 1] == s2[s2i - 1]:
                lcs[s2i][s1i] = lcs[s2i - 1][s1i - 1] + 1
            else:
                lcs[s2i][s1i] = max(lcs[s2i][s1i - 1], lcs[s2i - 1][s1i])
    
    return lcs[-1][-1]
    
print(commonChild('ABCD', 'ABDC'))
print(commonChild('HARRY', 'SALLY'))
print(commonChild('AA', 'BB'))
print(commonChild('SHINCHAN', 'NOHARAAA'))
print(commonChild('ABCDEF', 'FBDAMN'))