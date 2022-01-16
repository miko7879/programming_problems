class UF(object):

    def __init__(self, n):
        #Initialize parent and weight arrays
        self.parents = [x for x in range(n)]
        self.weights = [1]*n
        
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
        
    def union(self, p, q):
        #Get roots
        proot = self.root(p)
        qroot = self.root(q)
        #Attach smaller tree to root of larget tree
        if self.weights[proot] > self.weights[qroot]:
            self.parents[qroot] = proot
            self.weights[proot] += self.weights[qroot]
        else:
            self.parents[proot] = qroot
            self.weights[qroot] += self.weights[proot]
        
        
myUF = UF(10)
myUF.union(4, 3)
myUF.union(3, 8)
myUF.union(6, 5)
myUF.union(9, 4)
myUF.union(2, 1)
print(myUF.connected(0, 7))
print(myUF.connected(8, 9))
myUF.union(5, 0)
myUF.union(1, 6)
myUF.union(2, 7)
print(myUF.connected(0, 7))
        
    