def riddle(arr):

    max_windows = {}
    stack = []
    
    for i, n in enumerate(arr):
        
        if not stack or n > stack[-1][0]:
            stack.append((n, i))
        
        else:
            while stack and n < stack[-1][0]:
                num, index = stack.pop()
                if num not in max_windows:
                    max_windows[num] = i - index
                else:
                    max_windows[num] = max(max_windows[num], i - index)
            if not stack:
                stack.append((n, 0))
            elif n != stack[-1][0]:
                stack.append((n, index))
                
    while stack:
        num, index = stack.pop()
        if num not in max_windows:
            max_windows[num] = (len(arr) - index)
        else:
            max_windows[num] = max(max_windows[num], len(arr) - index)
            
    window_maxs = {}
    
    for key, value in max_windows.items():
        if value not in window_maxs:
            window_maxs[value] = key
        else:
            window_maxs[value] = max(window_maxs[value], key)
        
    ret = []
    prev = None
    for n in range(len(arr), 0, -1):
        if n in window_maxs:
            if not prev:
                prev = window_maxs[n]
            prev = max(window_maxs[n], prev)
        ret.append(prev)
        
    return ret[::-1]
    
print(riddle([6, 3, 5, 1, 12]))
print(riddle([2, 6, 1, 12]))
print(riddle([1, 2, 3, 5, 1, 13, 3]))
print(riddle([3, 5, 4, 7, 6, 2]))
print(riddle([789168277, 694294362, 532144299, 20472621, 316665904, 59654039, 685958445, 925819184, 371690486, 285650353, 522515445, 624800694, 396417773, 467681822, 964079876, 355847868, 424895284, 50621903, 728094833, 535436067, 221600465, 832169804, 641711594, 518285605, 235027997, 904664230, 223080251, 337085579, 5125280, 448775176, 831453463, 550142629, 822686012, 555190916, 911857735, 144603739, 751265137, 274554418, 450666269, 984349810, 716998518, 949717950, 313190920, 600769443, 140712186, 218387168, 416515873, 194487510, 149671312, 241556542, 575727819, 873823206]))