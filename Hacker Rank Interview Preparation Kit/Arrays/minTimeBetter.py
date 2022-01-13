import sys
from collections import Counter

def getItems(machineCounts, days):
    tot_items = 0
    for rate, numMachines in machineCounts.items():
        tot_items += (days//rate)*numMachines
    return tot_items

def minTime(machines, goal):
    nMachines = Counter(machines)
    minRate, maxRate = sys.maxsize, -sys.maxsize
    for rate in nMachines.keys():
        minRate = min(minRate, rate)
        maxRate = max(maxRate, rate)
    minDays, maxDays = (goal//len(machines) + int(goal%len(machines) != 0))*minRate, (goal//len(machines) + int(goal%len(machines) != 0))*maxRate
    while minDays <= maxDays:
        midDays = (minDays + maxDays)//2
        numItems = getItems(nMachines, midDays)
        if numItems >= goal:
            maxDays = midDays - 1
        else:
            minDays = midDays + 1
    return minDays

print(minTime([2, 3, 2], 10))   
print(minTime([2, 3], 5))   
print(minTime([1, 3, 4], 10)) 
print(minTime([4, 5, 6], 12))