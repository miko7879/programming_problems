def hgs(m, r, c):
    return m[r][c] + m[r][c + 1] + m[r][c + 2] + m[r + 1][c + 1] + m[r + 2][c] + m[r + 2][c + 1] + m[r + 2][c + 2]

def hourGlassSum(m):
    
    if len(m) < 2 or len(m[0]) < 2:
        return 0
        
    mx_sum = -sys.maxsize
        
    for r in range(len(m)- 2):
        for c in range(len(m[r]) - 2):
            mx_sum = max(mx_sum, hgs(m, r, c))
            
    return mx_sum
            
            
m = [[1, 1, 1, 0, 0, 0], [0, 1, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0], [0, 0, 2, 4, 4, 0], [0, 0, 0, 2, 0, 0], [0, 0, 1, 2, 4, 0]]
            
print(hourGlassSum(m))