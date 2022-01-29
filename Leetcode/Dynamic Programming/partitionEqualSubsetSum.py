def partitionEqualSubset(nums):
    
    ### Convert problem to 0/1 knapsack ###
    
    #Calculate the overall sum
    s = sum(nums)
    
    #If the sum is odd, can't do it
    if s % 2 == 1:
        return False
    
    #Calculate the target and store the length of the input array
    tgt = s//2
    n = len(nums)
    
    #Allocate memory for the cache, F(i, j): can we get sum i using the first j elements
    mem = [[False]*n for _ in range(tgt + 1)]
    
    ### Base cases ###
    
    #Can always get 0, F(0, j) = True for all j
    for i in range(n):
        mem[0][i] = True
        
    #Can always get the sum to equal to the first element using the first element, F[nums[0], 0] = True
    if nums[0] <= tgt:
        mem[nums[0]][0] = 1
    
    ### Transition ###
    
    #F(i, j) = F(i, j - 1) or 1(i - nums[j] >= 0)*F(i - nums[j], j - 1)
    for i in range(1, tgt + 1):
        for j in range(1, n):
            mem[i][j] = mem[i][j - 1] or (i - nums[j] >= 0 and mem[i - nums[j]][j - 1])
    
    #Return F(tgt, n)
    return mem[tgt][-1]
    
print(partitionEqualSubset([1, 5, 11, 5]))
print(partitionEqualSubset([1, 2, 3, 5]))        
    