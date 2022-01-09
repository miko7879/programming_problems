def getMedian(counts, buff_size):
    tgt_i = buff_size//2
    if buff_size % 2 == 0:
        tgt_i -= 1
    curr_i = 0
    curr_exp = 0
    while curr_i + counts[curr_exp] <= tgt_i:
        curr_i += counts[curr_exp]
        curr_exp += 1
    if buff_size % 2 == 1:
        return curr_exp
    first_exp = curr_exp
    tgt_i += 1
    while curr_i + counts[curr_exp] <= tgt_i:
        curr_i += counts[curr_exp]
        curr_exp += 1
    return (first_exp + curr_exp)/2
        

def activityNotifications(expenditure, d):
    countingSort = [0]*201
    for i in range(0, d):
        countingSort[expenditure[i]] += 1
    num_notifications = 0
    for i in range(d, len(expenditure)):
        med = getMedian(countingSort, d)
        if expenditure[i] >= 2*med:
            num_notifications += 1
        countingSort[expenditure[i - d]] -= 1
        countingSort[expenditure[i]] += 1
        
    return num_notifications
    
print(activityNotifications([10, 20, 30, 40, 50], 3)) 
print(activityNotifications([2, 3, 4, 2, 3, 6, 8, 4, 5], 5))
print(activityNotifications([1, 2, 3, 4, 4], 4)) 