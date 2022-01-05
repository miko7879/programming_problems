def sockMerchant(n, ar):
    
    seen = set()
    pairs = 0
    
    for n in ar:
        if n in seen:
            pairs += 1
            seen.remove(n)
        else:
            seen.add(n)
            
    return pairs
    
print(sockMerchant(9, [10, 20, 20, 10, 10, 30, 50, 10, 20]))