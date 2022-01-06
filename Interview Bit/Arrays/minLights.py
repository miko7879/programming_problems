def getLamp(A, min_i, i):
    
    i = min(i, len(A) - 1)

    while i >= min_i:
        if A[i] == 1:
            return i 
        i -= 1

    return -1
    
def minLights(A, B):

    cover = B - 1
    
    start = getLamp(A, 0, cover)
    
    if start == -1:
        return -1
        
    min_steps = 1
        
    while start + cover < len(A) - 1:
        start = getLamp(A, start + 1, start + 2*cover + 1)
        if start == -1:
            return -1
        min_steps += 1
        
    return min_steps
    
print(minLights([ 0, 0, 1, 1, 1, 0, 0, 1], 3))
print(minLights([ 0, 0, 0, 0, 0], 5))