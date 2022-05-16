import sys

#Interval class, essentially a tree node
class Interval(object):

    def __init__(self, s, e):
        self.start = s
        self.end = e
        self.subintervals = []
        
    def addint(self, other):
        self.subintervals.append(other)
        
    def isin(self, other):
        return other.start <= self.start and self.end <= other.end
        
    def getlist(self):
        if self.start == -sys.maxsize and self.end == sys.maxsize:
            return []
        return [self.start, self.end]
    
    def numin(self, n):
        return self.start <= n <= self.end
    
    def __repr__(self):
        return f'Interval: [{self.start}, {self.end}]'
        
    def __str__(self):
        return f'Interval: [{self.start}, {self.end}]'

#Define intervals      
intervals = [[2, 3], [1, 20], [15, 16], [2, 5], [1, 8], [9, 12], [6, 8]]
intervals = sorted(intervals, key = lambda x: (x[0], -x[1]))
intervals = [Interval(i[0], i[1]) for i in intervals]

#Build interval tree
root = Interval(-sys.maxsize, sys.maxsize)
s = [root]

for i in intervals:
    
    while not i.isin(s[-1]):
        s.pop()
        
    curr = s[-1]
    curr.addint(i)
    
    s.append(i)
  
#Define numbers
numbers = [3, 5, 7, 9, 15, 17, 40]

#Function to traverse tree and calculate optimal interval for a given number
def getBestInt(root, n):
    
    curr = root
    found_child = True
    
    while curr.numin(n) and found_child:
        
        found_child = False
        
        for i in curr.subintervals:
            if i.numin(n):
                found_child = True
                curr = i
                break
                
    return curr.getlist()

#Obtain optimal interval for each number
res = []

for n in numbers:

    res.append(getBestInt(root, n))
    
print(res)
    
    

    
