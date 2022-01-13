import heapq

def luckBalance(k, contests):
    losses = []
    tot_luck = 0
    for c in contests:
        luck, importance = c
        if importance == 0:
            tot_luck += luck
        else:
            if len(losses) < k:
                heapq.heappush(losses, luck)
            else:
                tot_luck -= heapq.heappushpop(losses, luck)
    return tot_luck + sum(losses)
    
print(luckBalance(2, [[5, 1], [1, 1], [4, 0]]))
print(luckBalance(3, [[5, 1], [2, 1], [1, 1], [8, 1], [10, 0], [5, 0]]))
        
         
            
