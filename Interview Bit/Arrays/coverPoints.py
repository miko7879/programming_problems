def coverPoints(A, B):
        
    num_steps = 0
        
    for i in range(1, len(A)):
        num_steps += max(abs(A[i] - A[i - 1]), abs(B[i] - B[i - 1]))

    return num_steps
    
print(coverPoints([0, 1, 1], [0, 1, 2]))