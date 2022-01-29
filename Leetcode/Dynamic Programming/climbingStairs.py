def climbingStairs(n):
    
    # mem[i]: number of ways to get to stair i
    mem = [0]*(n + 1)
    
    # mem[0] = 1 (only one way to not move), mem[1] = 1 (take one step)
    mem[0] = 1
    mem[1] = 1
    
    # mem[i] = mem[i - 1] + mem[i - 2] (to get to star i we can either take one step from the previous stair or two steps from the one before that) 
    for i in range(2, n + 1):
        mem[i] = mem[i - 1] + mem[i - 2]
        
    # answer is at mem[n]
    return mem[n]
    
print(climbingStairs(2))

print(climbingStairs(3))