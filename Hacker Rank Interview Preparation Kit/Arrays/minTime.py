import heapq
from collections import Counter

def minTime(machines, goal):
    nMachines = Counter(machines)
    machineQueue = []
    for m, count in nMachines.items():
        machineQueue.append((m, m, count))
    heapq.heapify(machineQueue)
    while goal > 0:
        complete_time, work_time, num_items = heapq.heappop(machineQueue)
        heapq.heappush(machineQueue, (complete_time + work_time, work_time, num_items))
        goal -= num_items
    return complete_time
        

print(minTime([2, 3, 2], 10))   
print(minTime([2, 3], 5))   
print(minTime([1, 3, 4], 10)) 
print(minTime([4, 5, 6], 12))