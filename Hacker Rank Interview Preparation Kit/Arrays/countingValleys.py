def countingValleys(steps, path):
    
    num_valleys = 0
    curr_height = 0
    in_valley = False
    
    for step in path:
        if step == 'D':
            curr_height -= 1
        else:
            curr_height += 1
        if curr_height < 0 and not in_valley:
            num_valleys += 1
            in_valley = True
        elif curr_height == 0 and in_valley:
            in_valley = False
            
    return num_valleys
    
print(countingValleys(12, 'DDUUUDDUDDUU'))