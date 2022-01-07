def binSearch(arr, tgt, l, r):

    if r < l:
        return l
        
    m = (l + r)//2
    
    if arr[m][0] < tgt:
        return binSearch(arr, tgt, m + 1, r)
    
    if arr[m][0] > tgt:
        return binSearch(arr, tgt, l, m - 1)
        
    return m + 1
    

def insert(existing, new):
    
    i = binSearch(existing, new[0], 0, len(existing) - 1)
    
    ret = existing[:i]
    
    if ret[-1][0] <= new[0] <= ret[-1][1]:
        ret[-1][1] = max(ret[-1][1], new[1])
    else:
        ret.append(new)
        
    for j in range(i, len(existing)):
        if ret[-1][0] <= existing[j][0] <= ret[-1][1]:
            ret[-1][1] = max(ret[-1][1], existing[j][1])
        else:
            ret = ret + existing[j:]
            break
            
    return ret
    
    
print(insert([[1,2],[3,6]],[8,10]))