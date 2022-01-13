def maximumToys(prices, k):
    num_toys = 0
    for n in sorted(prices):
        if n < k:
            num_toys += 1
            k -= n
        else:
            break
    return num_toys
    
print(maximumToys([1, 2, 3, 4], 7))
print(maximumToys([1, 12, 5, 111, 200, 1000, 10], 50))
    
