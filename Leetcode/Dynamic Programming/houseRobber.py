def houseRobber(nums):
        
    n = len(nums)
        
    # mem[i]: the maximum ammount that can be robbed if we stop at house i
    mem = [0]*(n + 1)
        
    # mem[0] = 0 (don't get anything if not robbing anything), mem[1] = nums[0] (just rob first house and stop)
    mem[1] = nums[0]
        
    # mem[i] = max(mem[i - 1], mem[i - 2] + nums[i - 1]): at each point, we can either rob the previous house or rob the current and the one before that
    for i in range(2, n + 1):
        mem[i] = max(mem[i - 2] + nums[i - 1], mem[i - 1])
            
    # answer is at mem[n]
    return mem[n]
    
print(houseRobber([1, 2, 3, 1]))
print(houseRobber([2, 7, 9, 3, 1]))