def zeroOneKanpsack(nums, tgt):

    if not tgt:
        return True
    
    mem = [[False]*len(nums) for _ in range(tgt + 1)]
    
    for i in range(0, len(nums)):
        mem[0][i] = True
    
    if nums[0] <= tgt:
        mem[nums[0]][0] = True
    
    for i in range(1, tgt + 1):
        for j in range(1, len(nums)):
            mem[i][j] = mem[i][j - 1] or (i - nums[j] >= 0 and mem[i - nums[j]][j - 1])
    
    return mem[tgt][-1]
    
print(zeroOneKanpsack([100, 5, 11, 5], 1))