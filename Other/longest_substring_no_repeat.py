from collections import OrderedDict

def lengthOfLongestSubstring(s):
    longest_substr = 0
    curr_substr = 0
    chars = OrderedDict()
    for c in s:
        if(c in chars):
            if(curr_substr > longest_substr):
                longest_substr = curr_substr
            while(True):
                curr_c = chars.popitem(last = False)
                curr_substr = curr_substr - 1
                if(curr_c[0] == c):
                    break
            chars[c] = True
            curr_substr += 1
        else:
            curr_substr += 1
            chars[c] = True
    if(curr_substr > longest_substr):
        longest_substr = curr_substr
    return longest_substr
    
print(lengthOfLongestSubstring("pwwkew"))