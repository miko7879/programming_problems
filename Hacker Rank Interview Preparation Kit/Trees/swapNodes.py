from collections import deque

def inOrder(indexes, i, res):
    if indexes[i][0] != -1:
        inOrder(indexes, indexes[i][0] - 1, res)
    res.append(i + 1)
    if indexes[i][1] != -1:
        inOrder(indexes, indexes[i][1] - 1, res)
    
def swapNodes(indexes, queries):
    res = []
    for query in queries:
        nodes = deque()
        nodes.append(indexes[0])
        curr_level = 1
        while nodes:
            new_nodes = deque()
            while nodes:
                curr = nodes.pop()
                if curr_level%query == 0:
                    tmp = curr[0]
                    curr[0] = curr[1]
                    curr[1] = tmp
                if curr[0] != -1:
                    new_nodes.append(indexes[curr[0] - 1])
                if curr[1] != -1:
                    new_nodes.append(indexes[curr[1] - 1])
            curr_level += 1
            nodes = new_nodes
        subres = []
        inOrder(indexes, 0, subres)
        res.append(subres)
    return res
        
print(swapNodes([[2, 3], [-1, -1], [-1, -1]], [1, 1]))
print(swapNodes([[2, 3], [4, 5], [6, -1], [-1, 7], [8, 9], [10, 11], [12, 13], [-1, 14], [-1, -1], [15, -1], [16, 17], [-1, -1], [-1, -1], [-1, -1], [-1, -1], [-1, -1], [-1, -1]], [2, 3]))
print(swapNodes([[2, 3], [4, -1], [5, -1], [6, -1], [7, 8], [-1, 9], [-1, -1], [10, 11], [-1, -1], [-1, -1], [-1, -1]], [2, 4]))