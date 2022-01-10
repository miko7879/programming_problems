def substrCount(n, s):
    
    curr = s[0]
    consec = 0
    counts = []
    
    for c in s:
        if c == curr:
            consec += 1
        else:
            counts.append((curr, consec))
            curr = c
            consec = 1
    counts.append((curr, consec))
       
    tot_subs = 0
    for i in range(len(counts)):
        tot_subs += (counts[i][1])*(counts[i][1] + 1)//2
        if 0 < i < len(counts) - 1 and counts[i - 1][0] == counts[i + 1][0] and counts[i][1] == 1:
            tot_subs += min(counts[i - 1][1], counts[i + 1][1])
        
    return tot_subs
        
print(substrCount(8, 'mnonopoo'))
print(substrCount(5, 'asasd'))   
print(substrCount(7, 'abcbaba'))
print(substrCount(4, 'aaaa'))
print(substrCount(11, 'aaacaadabba'))   
