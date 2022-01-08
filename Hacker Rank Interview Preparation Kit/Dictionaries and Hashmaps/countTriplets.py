from collections import defaultdict

def countTriplets(arr, r):
    
    freqs = defaultdict(int)
    for i, n in enumerate(arr):
        freqs[n] += 1
    
    pairs = []
    pairs_remain = defaultdict(int)
    for i, n in enumerate(arr):
        freqs[n] -= 1
        pairs.append(freqs[n*r])
        pairs_remain[n] += pairs[-1]
 
    trips = 0
    for i in range(len(arr) - 2):
        n = arr[i]
        pairs_remain[n] -= pairs[i]
        trips += pairs_remain[n*r]
        
    return trips

print(countTriplets([1, 4, 16, 64], 4))
print(countTriplets([1, 2, 2, 4], 2))
print(countTriplets([1, 3, 9, 9, 27, 81], 3))
print(countTriplets([1, 5, 5, 25, 125], 5))
print(countTriplets([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 1))