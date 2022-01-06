 def maxSubArray(self, A):

    #Kadane's Algorithm
    max_n = A[0]
    curr_s = 0
    for n in A:
        curr_s = max(curr_s + n, n)
        max_n = max(max_n, curr_s)

    return max_n