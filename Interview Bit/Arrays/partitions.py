def partitions(B):
    
    s = sum(B)
        
    if s % 3 != 0:
        return 0 

    tgt = s//3
    run_sum = 0
    num_ways = 0
        
    for i in range(0, len(B)):
        run_sum += B[i]
        if run_sum == tgt:
            sub_run_sum = 0
            for j in range(i + 1, len(B) - 1):
                sub_run_sum += B[j]
                if sub_run_sum == tgt:
                    num_ways += 1
                
    return num_ways
    
print(partitions([1, 2, 3, 0, 1, -1, 3]))