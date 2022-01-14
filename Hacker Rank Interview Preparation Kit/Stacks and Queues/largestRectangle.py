def largestRectangle(heights):
    
    stack = []
    max_area = 0
    
    for i, h in enumerate(heights):
        
        if not stack or stack[-1][0] < h:
            stack.append((h, i))
            
        else:
            while stack and h < stack[-1][0]:
                height, index = stack.pop()
                max_area = max(max_area, height*(i - index))
            if not stack:
                stack.append((h, 0))
            elif h != stack[-1][0]:
                stack.append((h, index))
                      
    while stack:
        height, index = stack.pop()
        max_area = max(max_area, height*(len(heights) - index))
            
    return max_area
    
print(largestRectangle([1, 2, 3, 4, 5]))
print(largestRectangle([1, 3, 4, 2]))
print(largestRectangle([3, 2, 3]))
print(largestRectangle([1, 3, 4, 2, 5,6, 7, 3, 1, 5, 8, 9, 10, 2, 1]))
    