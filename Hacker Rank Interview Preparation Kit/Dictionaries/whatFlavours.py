def whatFlavors(cost, money):
    seen = {}
    for i, c in enumerate(cost):
        if c in seen:
            print(f'{seen[c] + 1} {i + 1}')
            return 
        else:
            seen[money - c] = i
            
whatFlavors([2, 1, 3, 5, 6], 5)