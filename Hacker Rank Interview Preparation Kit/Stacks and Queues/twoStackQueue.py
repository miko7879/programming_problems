class MyQueue(object):

    def __init__(self):
        self.main = []
        self.aux = []
        
    def peek(self):
        if not self.aux:
            while self.main:
                self.aux.append(self.main.pop())
        if self.aux:
            return self.aux[-1]
        return None
        
    def pop(self):
        if not self.aux:
            while self.main:
                self.aux.append(self.main.pop())
        if self.aux:
            return self.aux.pop()
        return None
        
    def put(self, val):
        self.main.append(val)
        
q = MyQueue()

q.put(42)
print(q.pop())
q.put(14)
print(q.peek())
q.put(28)
print(q.peek())
q.put(60)
q.put(78)
print(q.pop())
print(q.pop())