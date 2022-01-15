import sys
from collections import deque

def findShortest(graph_nodes, graph_from, graph_to, ids, val):
    
    start_node = -1
    tot_nodes = 0
    for i, colour in enumerate(ids):
        if colour == val:
            tot_nodes += 1
            if start_node == -1:
                start_node = i + 1
                
    if tot_nodes < 2:
        return -1
    
    adj_list = [[] for _ in range(graph_nodes + 1)]
    for n1, n2 in zip(graph_from, graph_to):
        adj_list[n1].append(n2)
        adj_list[n2].append(n1)
        
    shortest_path = sys.maxsize
    bfs_seen = set()
    bfs_seen.add(start_node)
    bfs = deque()
    for neigh in adj_list[start_node]:
        bfs.append((neigh, 1))

    while bfs:
        curr_node, hops = bfs.pop()
        if curr_node in bfs_seen:
            continue
        bfs_seen.add(curr_node)
        if ids[curr_node - 1] == val:
            shortest_path = min(shortest_path, hops)
            hops = 0
        for neigh in adj_list[curr_node]:
            bfs.appendleft((neigh, hops + 1))
            
    return shortest_path  
        
    
        
    
    
print(findShortest(4, [1, 1, 4], [2, 3, 2], [1, 2, 1, 1], 1))
print(findShortest(4, [1, 1, 4], [2, 3, 2], [1, 2, 3, 4], 2))
print(findShortest(5, [1, 1, 2, 3], [2, 3, 4, 5], [1, 2, 3, 3, 2], 2))