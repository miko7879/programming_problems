def pickFromBothSides(A, B):

        i, j = B - 1, len(A) - 1

        curr_s = sum(A[:B])

        max_s = curr_s

        while i >= 0:
            curr_s = curr_s - A[i] + A[j]
            max_s = max(max_s, curr_s)
            i -= 1
            j -= 1

        return max_s

print(pickFromBothSides([5, -2, 3 , 1, 2], 3))
print(pickFromBothSides([1, 2], 1))
print(pickFromBothSides(\
[-533, -666, -500, 169, 724, 478, 358, -38, -536, 705, -855, 281, -173, 961, -509, -5, 942, -173, 436, -609, -396, 902, -847, -708, -618, 421, -284, 718, 895, 447, 726, -229, 538, 869, 912, 667, -701, 35, 894, -297, 811, 322, -667, 673, -336, 141, 711, -747, -132, 547, 644, -338, -243, -963, -141, -277, 741, 529, -222, -684, 35],\
48\
))