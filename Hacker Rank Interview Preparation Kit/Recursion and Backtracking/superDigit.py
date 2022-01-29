def superDigitHelper(n):
    
    if len(n) == 1:
        return int(n)
        
    return superDigitHelper(str(sum([int(c) for c in n]))) 

def superDigit(n, k):
    s = 0
    
    for c in n:
        s += int(c)
       
    return superDigitHelper(str(s*k))
    
    
print(superDigit('9875', 4))