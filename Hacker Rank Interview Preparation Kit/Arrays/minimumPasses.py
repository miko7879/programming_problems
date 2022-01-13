import math

def minimumPasses(m, w, p, n):
    
    #Purchasing is pointless if it costs more to buy than our target amount
    if p >= n:
        return math.ceil(n/(m*w))
        
    #Simulate game
    days = 0
    budget = 0
    while budget < n:
        
        #Determine today's rate
        rate = m*w
        
        #If won't generate enough candy in one day to purchase, run multiple days to collect enough candy
        if budget + rate < p:
            days_to_produce = math.ceil((p - budget)/rate)
            budget += rate*days_to_produce
            days += days_to_produce
        
        #Otherwise, run for one day
        else:
            budget += rate
            days += 1
            
        #Now that we have enough to purchase, let's determine optimal choice by seeing which decision results in the fewest remaining days after action is taken
        
        #Savings option
        days_left_save = (n - budget)/rate
        
        #Investing option - buy as much as possible
        can_buy = budget//p
        change = budget%p
        mn, mx = min(m, w), max(m, w)
        gap = mx - mn
        mn += min(can_buy, gap)
        can_buy -= gap
        if can_buy > 0:
            mx += can_buy//2
            mn += can_buy//2
            if can_buy%2 == 1:
                mx += 1
        days_left_invest = (n - change)/(mn*mx)
        
        #If it's more optimal to invest, do so and re-evaluate
        if days_left_save > days_left_invest:
            m, w, budget = mn, mx, change

        #Otherwise, continue to save, we can use this to stop early
        else:
            days += math.ceil(days_left_save)
            break
        
    return days
            
        
print(minimumPasses(1, 2, 1, 60))
print(minimumPasses(3, 1, 2, 12))
print(minimumPasses(1, 1, 6, 45))
print(minimumPasses(1, 100, 10000000000, 1000000000000))
print(minimumPasses(1, 1, 499999999999, 1000000000000))