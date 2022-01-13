from collections import deque

def balancedBrackets(s):
    myStack = deque()
    for c in s:
        if c == '(':
            myStack.append(')')
        elif c == '[':
            myStack.append(']')
        elif c == '{':
            myStack.append('}')
        else:
            if not myStack or c != myStack.pop():
                return 'NO'
    
    if myStack:
        return 'NO'
 
    return 'YES'
    
print(balancedBrackets('{[()]}'))
print(balancedBrackets('{[(])}'))
print(balancedBrackets('{{[[(())]]}}'))