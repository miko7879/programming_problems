def dfs(grid, visited, row, col):

    if visited[row][col] == 1 or grid[row][col] == 0:
        return 0
        
    visited[row][col] = 1
    ret = 1
    for dr, dc in ((-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)):
        if 0 <= row + dr < len(grid) and  0 <= col + dc < len(grid[0]):
            ret += dfs(grid, visited, row + dr, col + dc)
            
    return ret
    

def maxRegion(grid):
    
    visited = [[0]*len(grid[0]) for _ in range(len(grid))]
    max_region = 0
    
    for row in range(0, len(grid)):
        for col in range(0, len(grid[0])):
            if grid[row][col] == 1 and visited[row][col] == 0:
                max_region = max(max_region, dfs(grid, visited, row, col))
                
    return max_region
    
print(maxRegion([[1, 1, 0, 0], [0, 1, 1, 0], [0, 0, 1, 0], [1, 0, 0, 0]]))