def plusOne(A):

    #Introduct a carry of 1 to simulate adding 1
    carry = 1

    #Perform element-wise addition
    for j in range(len(A) - 1, -1, -1):
        s = A[j] + carry
        A[j] = s%10
        carry = s//10

    #Remove trailing zeroes
    if carry == 0:
        i = 0
        while A[i] == 0:
            i += 1
        return A[i:]

    #Tack on the final carry if necessary
    return [carry] + A
    
print(plusOne([9,9,9,9]))
print(plusOne([0,1,2,3]))
print(plusOne([7,6,9,1]))