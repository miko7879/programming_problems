def makeAnagram(a, b):

    ord_a = ord('a')
    
    a_chars = [0]*26
    for c in a:
        a_chars[ord(c) - ord_a] += 1
    
    b_chars = [0]*26    
    for c in b:
        b_chars[ord(c) - ord_a] += 1

    tot_remove = 0
    for i in range(26):
        tot_remove += abs(a_chars[i] - b_chars[i])
        b_chars[i] = 0
        
    return tot_remove + sum(b_chars)
    
print(makeAnagram('cde', 'abc'))
print(makeAnagram('cde', 'dcf'))