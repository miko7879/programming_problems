def arrayManipulation(n, queries):
    nums = [0]*n
    
    for query in queries:
        i, j, k = query
        nums[i - 1] += k
        if j < n:
            nums[j] -= k
            
    run_sum = 0
    max_val = nums[0]
    for num in nums:
        run_sum += num
        if num > 0:
            max_val = max(run_sum, max_val)
            
    return max_val

n1, q1 = 5, [(1, 2, 100), (2, 5, 100), (3, 4, 100)]
n2, q2 = 10, [(1, 5, 3), (4, 8, 7), (6, 9, 1)]
n3, q3 = 10, [(2, 6, 8), (3, 5, 7), (1, 8, 1), (5, 9, 15)]

print(arrayManipulation(n1, q1))
print(arrayManipulation(n2, q2))
print(arrayManipulation(n3, q3))