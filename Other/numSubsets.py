from collections import defaultdict

def numSubsets(arr, tgt):
    
    subsets = defaultdict(int)
    
    for n in arr:
        if n > tgt:
            continue
        keys = list(subsets.keys())
        for key in keys:
            if key + n <= tgt:
                subsets[key + n] += subsets[key]
        subsets[n] += 1
        
    return subsets[tgt]
    
print(numSubsets([2, 4, 6, 10], 16))