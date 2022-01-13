def minBribes(q):

    num_bribes = 0
    
    times_bribed= [0]*len(q)
    orig_pos = [i + 1 for i in range(len(q))]
    
    for i, n in enumerate(q):
        offset = n - i - 1 + times_bribed[n - 1]
        
        if offset < 0:
            print("Error!")
            print(i, n, offset)
            print(orig_pos)
            print(times_bribed)
            return
        
        if offset > 2:
            print("Too Complicated!")
            return
        
        num_bribes += offset
        
        for j in range(offset - 1, -1, -1):
            times_bribed[orig_pos[i + j] - 1] += 1
            orig_pos[i + j + 1] = orig_pos[i + j]
            
    print(num_bribes)
    
    
minBribes([2, 1, 5, 3, 4])
minBribes([1, 2, 5, 3, 4, 7, 8, 6])
minBribes([2, 5, 1, 3, 4])
    