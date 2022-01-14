def poisonousPlants(p):

    stack = [(p[0], 0)]
    max_days = 0
    curr_min = p[0]
    
    for i in range(1, len(p)):
        
        if p[i] <= curr_min:
            curr_min = p[i]
            stack = [(p[i], 0)]
            continue
        
        extra_days = 1
        while p[i] <= stack[-1][0]:
            extra_days = max(extra_days, stack.pop()[1] + 1)
        max_days = max(max_days, extra_days)
        stack.append((p[i], extra_days))
        
    return max_days
            
        
        
    
    
print(poisonousPlants([5, 8, 4, 7, 10, 9]))
print(poisonousPlants([3, 6, 2, 7, 5]))
print(poisonousPlants([1, 1, 1, 1, 1]))
print(poisonousPlants([1, 2, 3, 4, 5]))