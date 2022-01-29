import functools

def lastStoneWeightII(stones):
    
    @functools.lru_cache()
    def canSum(tgt, i):
        
        if tgt == 0:
            return True
        
        if tgt < 0 or i == len(stones):
            return False
        
        return canSum(tgt - stones[i], i + 1) or canSum(tgt, i + 1)
    
    if not stones:
        return 0
    
    if len(stones) == 1:
        return stones[0]
    
    s = sum(stones)
    
    for tgt in range(s//2, -1, -1):
        if canSum(tgt, 0):
            return s - tgt - tgt
        
        
print(lastStoneWeightII([2,7,4,1,8,1]))
print(lastStoneWeightII([31,26,33,21,40]))