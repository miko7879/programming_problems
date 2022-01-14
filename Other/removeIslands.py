#[1, 0, 0, 0, 0, 0]
#[0, 1, 0, 1, 1, 1]
#[0, 0, 1, 0, 1, 0]
#[1, 1, 0, 0, 1, 0]
#[1, 0, 1, 1, 0, 0]
#[1, 0, 0, 0, 0, 1]

def dfs(m, visited, r, c):

    if visited[r][c] == 1 or m[r][c] == 0:
        return
    
    visited[r][c] = 1
    
    for dr, dc in ((-1, 0), (0, -1), (1, 0), (0, 1)):
        
        if not 0 <= r + dr < len(m) or not 0 <= c + dc < len(m[0]):
            continue
            
        dfs(m, visited, r + dr, c + dc)
    

def removeIslands(m): # m is R^(pxq)
    
    #O(pxq)
    visited = [[0]*len(m[0]) for _ in range(len(m))]
    
    #O(pxq)
    
    for col in range(len(m[0])):
        dfs(m, visited, 0, col)
        dfs(m, visited, len(m) - 1, col)
        
    for row in range(1, len(m) - 1):
        dfs(m, visited, row, 0)
        dfs(m, visited, row, len(m[0]) - 1)
        
    #O(pxq)
        
    for row in range(1, len(m) - 1):
        for col in range(1, len(m[0]) - 1):
            if m[row][col] == 1 and visited[row][col] == 0:
                m[row][col] = 0
                
    return m
    
    
#Overall runtime: O(pxq)
    
print(removeIslands([[1, 0, 0, 0, 0, 0], [0, 1, 0, 1, 1, 1], [0, 0, 1, 0, 1, 0], [1, 1, 0, 0, 1, 0], [1, 0, 1, 1, 0, 0], [1, 0, 0, 0, 0, 1]]))