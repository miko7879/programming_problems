def triplets(a, b, c):
    a.sort()
    b.sort()
    c.sort()
    a_ptr, a_count = 0, 0
    c_ptr, c_count = 0, 0
    tot_pairs = 0
    seen = set()
    for n in b:
        if n in seen:
            continue
        seen.add(n)
        while a_ptr < len(a) and a[a_ptr] <= n:
            if a_ptr == 0 or a[a_ptr] != a[a_ptr - 1]:
                a_count += 1
            a_ptr += 1
        while c_ptr < len(c) and c[c_ptr] <= n:
            if c_ptr == 0 or c[c_ptr] != c[c_ptr - 1]:
                c_count += 1
            c_ptr += 1
        tot_pairs += a_count*c_count
    return tot_pairs
    
print(triplets([3, 5, 7], [3, 6], [4, 6, 9]))
print(triplets([1, 3, 5], [2, 3], [1, 2, 3]))
print(triplets([1, 4, 5], [2, 3, 3], [1, 2, 3]))
print(triplets([1, 3, 5, 7], [5, 7, 9], [7, 9, 11, 13]))