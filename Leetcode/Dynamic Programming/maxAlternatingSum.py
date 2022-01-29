import time

def maxAlternatingSum(nums):
        
    n = len(nums)
        
    # mem[i, op]: the maximum alternating subsequence sum up to element i depending on whether we are adding or subtracting next
    mem = [[0, 0] for _ in range(n)]
        
    # mem[i, add] = mem[i, 0], mem[i, sub] = mem[i, 1]
    add, sub = 0, 1
        
    # mem[0, add]: 0, mem[0, sub]: nums[0]
    mem[0][sub] = nums[0]
        
    # mem[i, add] = max(mem[i - 1, add], mem[i - 1, sub] - nums[i]), mem[i, sub] = max(mem[i - 1], sub, mem[i - 1, add] + nums[i])
    for i in range(1, n):
        mem[i][add] = max(mem[i - 1][add], mem[i - 1][sub] - nums[i])
        mem[i][sub] = max(mem[i - 1][sub], mem[i - 1][add] + nums[i])
        
    # answer will always be in mem[n, sub] since that means the last action was an addition
    return mem[n - 1][sub]
    
def maxAlternatingSumOpt(nums):
        
    # mem[i, op]: the maximum alternating subsequence sum up to element i depending on whether we are adding or subtracting next
    mem = [0, 0]
        
    # mem[i, add] = mem[i, 0], mem[i, sub] = mem[i, 1]
    add, sub = 0, 1
        
    # mem[0, add]: 0, mem[0, sub]: nums[0]
    mem[sub] = nums[0]
        
    # mem[i, add] = max(mem[i - 1, add], mem[i - 1, sub] - nums[i]), mem[i, sub] = max(mem[i - 1], sub, mem[i - 1, add] + nums[i])
    for i in range(1, len(nums)):
        prev_add, prev_sub = mem[add], mem[sub]
        mem[add] = max(prev_add, prev_sub - nums[i])
        mem[sub] = max(prev_sub, prev_add + nums[i])
        
    # answer will always be in mem[n, sub] since that means the last action was an addition
    return mem[sub]


print(maxAlternatingSum([4, 2, 5, 3]))
print(maxAlternatingSum([5, 6, 7, 8]))
print(maxAlternatingSum([6, 2, 1, 2, 4, 5, 12, 4, 15, 151, 12, 912, 4139, 1324, 132, 23, 42]))

print('--------------')

print(maxAlternatingSumOpt([4, 2, 5, 3]))
print(maxAlternatingSumOpt([5, 6, 7, 8]))
print(maxAlternatingSum([6, 2, 1, 2, 4, 5, 12, 4, 15, 151, 12, 912, 4139, 1324, 132, 23, 42]))