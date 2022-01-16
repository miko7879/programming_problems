class UF(object):

    def __init__(self, n, machines):
        #Initialize parent and weight arrays
        self.parents = [x for x in range(n)]
        self.weights = [1]*n
        m = set(machines)
        self.hasMachine = [True if x in m else False for x in range(n)]
        
    def root(self, i):
        #Get Root
        r = i
        while self.parents[r] != r:
            r = self.parents[r]
        #Path compression
        while self.parents[i] != r:
            nxt = self.parents[i]
            self.parents[i] = r
            i = nxt
        #Return the root
        return r
        
    def connected(self, p, q):
        return self.root(p) == self.root(q)
        
    def containsMachine(self, p):
        return self.hasMachine[self.root(p)]
        
    def union(self, p, q):
        #Get roots
        proot = self.root(p)
        qroot = self.root(q)
        #Attach smaller tree to root of larget tree
        if self.weights[proot] > self.weights[qroot]:
            self.parents[qroot] = proot
            self.weights[proot] += self.weights[qroot]
            if self.hasMachine[qroot]:
                self.hasMachine[proot] = True
        else:
            self.parents[proot] = qroot
            self.weights[qroot] += self.weights[proot]
            if self.hasMachine[proot]:
                self.hasMachine[qroot] = True
                
                
def minTime(roads, machines):
    disjointSet = UF(len(roads) + 1, machines)
    tot_cost = 0
    for c1, c2, cost in sorted(roads, key = lambda x: x[2], reverse = True):
        if not disjointSet.containsMachine(c1) or not disjointSet.containsMachine(c2):
            disjointSet.union(c1, c2)
        else:
            tot_cost += cost
    return tot_cost
    
print(minTime([[0, 1, 4], [1, 2, 3], [1, 3, 7], [0, 4, 2]], [2, 3, 4]))