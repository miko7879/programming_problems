from collections import deque

def removeInvalidParentheses(s):
    
    n_close = 0
    close_left = [0]*len(s)
    for i in range(len(s) - 1, -1, -1):
        if s[i] == ')':
            n_close += 1
        close_left[i] = n_close
    
    res, mxlen = set(), 0
    
    candidates = deque()
    candidates.append(('', 0, 0))
    
    while candidates:
        
        curr_s, num_open, i = candidates.pop()
        
        if num_open == 0:
            if len(curr_s) > mxlen:
                res, mxlen = set(), len(curr_s)
            if len(curr_s) == mxlen:
                res.add(curr_s)
            
        if i == len(s) or num_open > close_left[i]:
            continue
            
        ch = s[i]
        
        if ch not in ('(', ')'):
            candidates.appendleft((curr_s + ch, num_open, i + 1))
            continue
        
        elif ch == '(':
            candidates.appendleft((curr_s + ch, num_open + 1, i + 1))
        
        elif num_open > 0:
            candidates.appendleft((curr_s + ch, num_open - 1, i + 1))
        
        candidates.appendleft((curr_s, num_open, i + 1))
        
    return res
    
print(removeInvalidParentheses('()())()'))
print(removeInvalidParentheses('(a)())()'))