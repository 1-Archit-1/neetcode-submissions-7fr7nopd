class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s) == 0:
            return 0 
        l = 0 
        r = 1 

        freq = {s[l] : 1} 
        maxf = 1 

        res = 1
        while r < len(s):
            freq[s[r]] = 1+ freq.get(s[r], 0 )
            maxf = max(maxf, freq[s[r]])

            if r-l+1 -maxf > k:
                while r-l+1 -maxf > k:
                    freq[s[l]]-=1 
                    l+=1 
        
            res = max(res, r-l+1)
            r+=1
        return res

