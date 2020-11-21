a = "abcabcbb12345"
def longestSubstring(a):
    # def lengthOfLongestSubstring(self, a: str) -> int:
    if len(a.strip()) == 0:
        print(0)
    # lenSubstring = 0
    left = 0
    right = 0
    maxLen = 0
    for ch in range(len(a)):
        char = a[ch] 
        if(char not in a[left:right]):
            right += 1
        else:
            if(maxLen < (right - left )):
                maxLen = (right - left )
            
            lastoccurance = a.find(char,left,ch)
            left = lastoccurance+1
            right = ch+1
        
    if(maxLen<(right - left )):
        maxLen = (right - left )
    return maxLen

print(longestSubstring(a))