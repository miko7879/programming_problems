def countPalindromicSubstrings(s):

    ret = 0
    
    for i in range(0, len(s)):
        
        ret += 1
        l, r, = i - 1, i + 1
        while l >= 0 and r < len(s) and s[l] == s[r]:
            ret += 1
            l -= 1
            r += 1
        
    for i1 in range(0, len(s) - 1):
        
        i2 = i1 + 1
        
        if s[i2] != s[i1]:
            continue
        
        ret += 1
        l, r = i1 - 1, i2 + 1
        while l >= 0 and r < len(s) and s[l] == s[r]:
            ret += 1
            l -= 1
            r += 1
        
    return ret
    
print(countPalindromicSubstrings('abc'))
print(countPalindromicSubstrings('aaa'))