def stepPermsHelper(n, c):

    if n == 1:
        return 1
    
    if n == 2:
        return 2
        
    if n == 3:
        return 4
        
    if n not in c:
        c[n] = stepPermsHelper(n - 1, c) + stepPermsHelper(n - 2, c) + stepPermsHelper(n - 3, c)
        
    return c[n]

def stepPerms(n):
    
    return stepPermsHelper(n, {})
    
def stepPermsBU(n):
    
    stepPerms = [0]*(n + 1)
    
    stepPerms[1] = 1
    stepPerms[2] = 2
    stepPerms[3] = 4
    
    for i in range(4, n + 1):
        stepPerms[i] = stepPerms[i - 1] + stepPerms[i - 2] + stepPerms[i - 3]
        
    return stepPerms[-1]
    
    
print(stepPerms(1))
print(stepPerms(4))
print(stepPerms(7))
print(stepPerms(100))
print(stepPermsBU(1000))