from collections import defaultdict

def freqQuery(queries):

    nums, freqs = defaultdict(int), defaultdict(int)

    ret = []

    for q in queries:
        
        ty = q[0]
        n = q[1]
        
        if ty == 1:
            freqs[nums[n]] -= 1
            nums[n] += 1
            freqs[nums[n]] += 1
            
        elif ty == 2:
            if nums[n] == 0:
                continue
            freqs[nums[n]] -= 1
            nums[n] -= 1
            freqs[nums[n]] += 1
            
        else:
            ret.append(int(freqs[n] > 0))
            
        #print(ty, n)
        #print(nums)
        #print(freqs)
        #print()
        
    return ret
        
queries = [(1, 5), (1, 6), (3, 2), (1, 10), (1, 10), (1, 6), (2, 5), (3, 2)]

print(freqQuery(queries))