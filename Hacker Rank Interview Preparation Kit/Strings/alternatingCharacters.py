def alternatingCharacters(s):
    num_deletions = 0
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            num_deletions += 1
    return num_deletions


print(alternatingCharacters('AABAAB'))    
print(alternatingCharacters('AAAA'))
print(alternatingCharacters('BBBBB'))
print(alternatingCharacters('ABABABAB'))
print(alternatingCharacters('BABABA'))
print(alternatingCharacters('AAABBB'))