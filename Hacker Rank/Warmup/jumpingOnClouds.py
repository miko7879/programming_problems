def jumpingOnClouds(c):
    
    steps = 0
    curr = 0
    
    while curr != len(c) - 1:
        
        if curr + 2 >= len(c) or c[curr + 2] == 1:
            curr += 1
        else:
            curr += 2
        
        steps += 1
        
    return steps
    
print(jumpingOnClouds([0, 0, 1, 0, 0, 1, 0]))
print(jumpingOnClouds([0, 0, 0, 1, 0, 0]))