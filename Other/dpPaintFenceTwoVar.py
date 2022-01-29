def paintFence(n):

    mem = [[1, 2] + [0]*(n - 1) for _ in range(2)]

    for i in range(2, n + 1):
        mem[0][i] = mem[1][i - 1] + mem[1][i - 2]
        mem[1][i] = mem[0][i - 1] + mem[0][i - 2]
        
    return mem[0][n] + mem[1][n]
    
print(paintFence(4))
print(paintFence(5))
print(paintFence(1000))