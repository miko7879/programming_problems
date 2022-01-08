def twoStrings(a, b):
    chars_b = set(b)
    for c in a:
        if c in chars_b:
            return "YES"
    return "NO"
    
print(twoStrings('hello', 'world'))
print(twoStrings('hi', 'world'))