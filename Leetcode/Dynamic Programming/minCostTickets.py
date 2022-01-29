import sys

def minCostTickets(days, costs):
    
    mem = [0]*(days[-1] + 1)
    
    travel_days = set(days)
    
    pass_duration = (1, 7, 30)
    
    for day in range(1, days[-1] + 1):
        if day in travel_days:
            cost = sys.maxsize
            for pass_type in (0, 1, 2):
                cost = min(cost, mem[max(day - pass_duration[pass_type], 0)] + costs[pass_type])
            mem[day] = cost
        else:
            mem[day] = mem[day - 1]
        
    return mem[days[-1]]
    
print(minCostTickets([1,2,3,4,5,6,7,8,9,10,30,31], [2,7,15]))
print(minCostTickets([1,4,6,7,8,20], [2,7,15]))
print(minCostTickets([1,4,6,7,8,20], [7,2,15]))