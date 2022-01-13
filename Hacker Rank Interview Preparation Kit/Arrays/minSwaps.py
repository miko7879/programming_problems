def swap(inds, arr, i1, i2):
    tmp = inds[i1]
    inds[i1] = inds[i2]
    inds[i2] = tmp
    tmp = arr[inds[i1]]
    arr[inds[i1]] = arr[inds[i2]]
    arr[inds[i2]] = tmp

def minSwaps(arr):
    inds = [0]*len(arr)
    for i, n in enumerate(arr):
        inds[n - 1] = i
        
    n_swaps = 0
    for i in range(len(arr)):
        n = arr[i]
        if inds[i] == i:
            continue
        n_swaps += 1
        swap(inds, arr, n - 1, i)
        
    return n_swaps

    
print(minSwaps([2, 3, 4, 1, 5]))
print(minSwaps([7, 1, 3, 2, 4, 5, 6]))
print(minSwaps([4, 3, 1, 2]))
print(minSwaps([1, 3, 5, 4, 2, 6, 7]))