from collections import deque

class Graph(object):
    
    def __init__(self, n):
        self.n = n
        self.adj_list = [[] for _ in range(n)]
        
    def connect(self, n1, n2):
        self.adj_list[n1].append(n2)
        self.adj_list[n2].append(n1)
        
    def find_all_distances(self, start):
        
        distances = [-1]*self.n
        bfs_seen = set()
        bfs_seen.add(start)
        bfs = deque()
        
        for nei in self.adj_list[start]:
            bfs.append((nei, 1))
            
        while bfs:
            
            node, dist = bfs.pop()
            
            if node in bfs_seen:
                continue
            
            bfs_seen.add(node)
            distances[node] = dist*6
            
            for nei in self.adj_list[node]:
                if nei not in bfs_seen:
                    bfs.appendleft((nei, dist + 1))
        
        res = distances[:start] + distances[start + 1:]
        
        print(*res)
            
        
        

t = int(input())
for i in range(t):
    n,m = [int(value) for value in input().split()]
    graph = Graph(n)
    for i in range(m):
        x,y = [int(x) for x in input().split()]
        graph.connect(x-1,y-1) 
    s = int(input())
    graph.find_all_distances(s-1)