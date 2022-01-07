def flip(A):

    wl,wr = 0, 0
    nums = [0, 0]
    max_gain = 0
    ret = []
    
    while wr < len(A):
    
        nums[ord(A[wr]) - ord('0')] += 1
        
        if A[wr] == '0':
            if nums[0] - nums[1] > max_gain:
                max_gain = nums[0] - nums[1]
                ret =[wl + 1, wr + 1]
                
        if nums[0] < nums[1]:
            wl = wr
            while wl < len(A) and A[wl] == '1':
                wl += 1
            wr = wl
            nums[0], nums[1] = 1, 0
            if wl < len(A) and nums[0] - nums[1] > max_gain:
                ret = [wl + 1, wl + 1]
        
        wr += 1
     
    return ret
                
    
    


print(flip("1101"))