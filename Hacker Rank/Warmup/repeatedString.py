def repeatedString(s, n):
    
    num_a = 0
    
    for c in s:
        
        if c == 'a':
            num_a += 1
            
    fits = n//len(s)
    remain = n%len(s)
    
    tot_a = fits*num_a
    
    for j in range(0, remain):
        if s[j] == 'a':
            tot_a += 1
    
    return tot_a
    
    
print(repeatedString('a', 1000000000000))
print(repeatedString('aba', 10))
print(repeatedString('abcac', 1))
print(repeatedString('abcac', 0))
print(repeatedString('abcac', 4))
print(repeatedString('abcac', 8))
print(repeatedString('abcac', 9))
print(repeatedString('abcac', 10))
print(repeatedString('abcac', 14))