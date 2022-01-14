inputs = [
    [1, 0, 0, 0, 1],
    [1, 1, 0, 0, 1],
    [0, 1, 1, 0, 1],
    [0, 0, 0, 0, 0],
    [1, 0, 1, 1, 1]
]

def visit(i, j, inputs, visited):
    visited[i][j] = True
    if(inputs[i][j] == 0):
        return 0
    size = 1;
    if(i - 1 >= 0 and visited[i - 1][j] == False):
        size += visit(i - 1, j, inputs, visited)
    if(i + 1 < len(inputs) and visited[i + 1][j] == False):
        size += visit(i + 1, j, inputs, visited)
    if(j - 1 >= 0 and visited[i][j - 1] == False):
        size += visit(i, j - 1, inputs, visited)
    if(j + 1 < len(inputs[i]) and visited[i][j + 1] == False):
        size += visit(i, j + 1, inputs, visited)
    return size

river_sizes = []
visited = []
for i in range(len(inputs)):
    visited.append([False]*len(inputs[i]))
    
for i in range(len(inputs)):
    for j in range(len(inputs[i])):
        if(inputs[i][j] == 1 and visited[i][j] == False):
            river_sizes.append(visit(i, j, inputs, visited))
            
print(river_sizes)