from collections import defaultdict

def sherlockAnagrams(s):
    
    seen = defaultdict(int)
    
    anagrams = 0
    
    for i in range(len(s)):
        curr = [0]*26
        for j in range(i, len(s)):
            curr[ord(s[j]) - ord('a')] += 1
            key = tuple(curr)
            anagrams += seen[key]
            seen[key] += 1
            
    return anagrams
    
print(sherlockAnagrams('mom'))   
print(sherlockAnagrams('abba'))
print(sherlockAnagrams('abcd'))
print(sherlockAnagrams('ifailuhkqq'))
print(sherlockAnagrams('kkkk'))
print(sherlockAnagrams('cdcd'))