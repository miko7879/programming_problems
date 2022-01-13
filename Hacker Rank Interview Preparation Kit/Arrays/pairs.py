def pairs(k, arr):
    arr.sort()
    l, r = 0, 1
    num_pairs = 0
    while r < len(arr):
        while arr[r] - arr[l] >= k and l < r:
            if arr[r] - arr[l] == k:
                num_pairs += 1
            l += 1
        r += 1
    return num_pairs
    
