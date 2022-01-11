from collections import Counter
from collections import defaultdict
from collections import deque

def reverseShuffleMerge(s):
    
    counts = Counter(s)
    targets = defaultdict(int)
    for key, value in counts.items():
        targets[key] = value//2
    
    res = deque()
    
    for c in reversed(s):
        counts[c] -= 1
        if targets[c] == 0:
            continue
        while res and res[-1] > c and counts[res[-1]] > targets[res[-1]]:
            targets[res.pop()] += 1
        res.append(c)
        targets[c] -= 1
        
    return ''.join(res)
    
print(reverseShuffleMerge('abab'))
print(reverseShuffleMerge('eggegg'))
print(reverseShuffleMerge('abcdefgabcdefg'))
print(reverseShuffleMerge('aeiouuoiea'))
    
    