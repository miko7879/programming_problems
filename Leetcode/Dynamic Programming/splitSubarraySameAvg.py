import time
import functools

def splitArraySameAverage(nums):
    
    def canSum(tgt, remaining, i, nums, c):
        
        if remaining == 0:
            return tgt == 0
            
        if tgt < 0 or remaining + i > len(nums):
            return False
            
        if (tgt, remaining, i) not in c:
            c[(tgt, remaining, i)] = canSum(tgt - nums[i], remaining - 1, i + 1, nums, c) or canSum(tgt, remaining, i + 1, nums, c)
            
        return c[(tgt, remaining, i)]
        
    n, s, cache = len(nums), sum(nums), {}
    
    for tgt_n in range(1, n//2 + 1):
        if s*tgt_n % n == 0 and canSum(s*tgt_n//n, tgt_n, 0, nums, cache):
            return True
            
    return False

st = time.time()
print(splitArraySameAverage([4, 4, 4, 4, 4, 4, 5, 4, 4, 4, 4, 4, 4, 5]))
print(splitArraySameAverage([11, 20, 2, 19, 3]))
print(splitArraySameAverage([3863,703,1799,327,3682,4330,3388,6187,5330,6572,938,6842,678,9837,8256,6886,2204,5262,6643,829,745,8755,3549,6627,1633,4290,7]))
print(f'Time taken: {time.time() - st}')

