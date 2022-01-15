def getCluster(adj_list, city, clust):
    clust.add(city)
    for adj_city in adj_list[city]:
        if adj_city not in clust:
            getCluster(adj_list, adj_city, clust) 


def roadsAndLibraries(n, c_lib, c_road, cities):
    
    if c_road >= c_lib:
        return n*c_lib
    
    adj_list = [[] for _ in range((n + 1))]
    for c1, c2 in cities:
        adj_list[c1].append(c2)
        adj_list[c2].append(c1)
        
    tot_cost = 0
    already_accessible = set()
    for city in range(1, n + 1):
        if city in already_accessible:
            continue
        clust = set()
        getCluster(adj_list, city, clust) 
        tot_cost += (len(clust) - 1)*c_road + c_lib
        already_accessible.update(clust)

    return tot_cost
        
    
print(roadsAndLibraries(3, 2, 1, [[1, 2], [3, 1], [2, 3]]))
    