### If testing on HackerRank make sure you use Pypy3 instead of Python 3
### This algorithm is O(nlogn) but may time out if testing in Python 3, will work fine in Pypy3


from collections import deque

#This function will merge two arrays and count the number of required inversions to do so
def merge(a1, a2):
    ret = [0]*(len(a1) + len(a2))
    i1, i2 = 0, 0
    num_inversions = 0
    while i1 < len(a1) or i2 < len(a2):
        if i1 < len(a1) and (i2 == len(a2) or a1[i1] <= a2[i2]):
            ret[i1 + i2] = a1[i1]
            i1 += 1
        else:
            ret[i1 + i2] = a2[i2]
            i2 += 1
            num_inversions += len(a1) - i1
    return ret, num_inversions
    
def countInversions(arr):
    
    #Deque to store all sublists
    sublists = deque()
    
    #Checking if array is already sorted
    is_sorted = True
    
    #Split the array into constituent parts
    for i, n in enumerate(arr):
        sublists.append([n])
        if i > 0 and n < arr[i - 1]:
            is_sorted = False
           
    #Sorted array, nothing to do
    if is_sorted:
        return 0
    
    #Variable to keep track of the number of inversiosn
    num_inversions = 0
        
    #Use a while loop and a deque to ensure appropriate merging order
    while len(sublists) > 1:
        
        #Deque to store next set of arrays, again to ensure appropriate order
        new_sublists = deque()
        
        #Generate next set of arrays, count number of inversions
        while sublists:
            if len(sublists) > 1:
                merged, inversions = merge(sublists.popleft(), sublists.popleft())
            else:
                merged, inversions = merge(new_sublists.pop(), sublists.popleft())
            num_inversions += inversions
            new_sublists.append(merged)
        
        #Update the sublist deque
        sublists = new_sublists
    
    #Return the number of inversions
    return num_inversions
    
print(countInversions([1, 1, 1, 2, 2]))
print(countInversions([2, 1, 3, 1, 2]))
print(countInversions([2, 4, 1]))