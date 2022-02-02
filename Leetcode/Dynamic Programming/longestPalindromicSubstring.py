def longestPalindromicSubstring(s):

    mx_len = 0
    
    for i in range(0, len(s)):
        
        curr_len = 1
        l, r, = i - 1, i + 1
        while l >= 0 and r < len(s) and s[l] == s[r]:
            curr_len += 2
            l -= 1
            r += 1
            
        mx_len = max(curr_len, mx_len)
        
    for i1 in range(0, len(s) - 1):
        
        i2 = i1 + 1
        
        if s[i2] != s[i1]:
            continue
        
        curr_len = 2
        l, r = i1 - 1, i2 + 1
        while l >= 0 and r < len(s) and s[l] == s[r]:
            curr_len += 2
            l -= 1
            r += 1
            
        mx_len = max(curr_len, mx_len)
        
    return mx_len
    
print(longestPalindromicSubstring('babad'))
print(longestPalindromicSubstring('cbbd'))