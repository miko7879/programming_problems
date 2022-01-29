def findTargetSumWays(nums, target):

    def numSum(prevSum, tgt, i, nums, c):
            
        if i == len(nums):
                
            if prevSum == tgt:
                return 1
                
            return 0
            
        if (prevSum, i) not in c:
            c[(prevSum, i)] = numSum(prevSum + nums[i], tgt, i + 1, nums, c) + numSum(prevSum - nums[i], tgt, i + 1, nums, c)
            
        return c[(prevSum, i)]
        
    return numSum(0, target, 0, nums, {})
    
print(findTargetSumWays([1,1,1,1,1], 3))

print(findTargetSumWays([1], 1))

print(findTargetSumWays([4, 7, 8], 1))    