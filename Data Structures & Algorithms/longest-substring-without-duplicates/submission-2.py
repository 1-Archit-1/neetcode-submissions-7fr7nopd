class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0 
        r = 1 
        if len(s) == 0:
            return 0
        last_index = {}
        last_index[s[l]] = l 
        maxlen = float("-inf")
        while r< len(s):
            if last_index.get(s[r]) is not None and last_index[s[r]]>=l :
                maxlen = max (maxlen, r-l)
                l = last_index[s[r]]+1 
            last_index[s[r]] = r
            r+=1 

        return max(maxlen, r-l )
                

