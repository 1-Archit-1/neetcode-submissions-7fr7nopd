class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l = 0 
        r = 0 
    
        countT, countW = {}, {} 

        for ch in t:
            countT[ch] = countT.get(ch,0) +1 
        
        count = len(countT)
        have = 0 
        minlen = float("inf")
        res = "" 
        while r<len(s):
            if countT.get(s[r], 0) > 0:
                countW[s[r]] = countW.get(s[r],0) +1 
                if countW.get(s[r]) == countT.get(s[r]):
                    have+=1 
                while have == count: 
                    currl = r-l+1 
                    if s[l] in countW:
                        countW[s[l]] -=1 
                        if countW[s[l]] < countT[s[l]]:
                            have-=1 
                    l+=1
                    if currl < minlen:
                        res = s[l-1: r+1]
                        minlen = currl 

            r+=1 
        return res 
                
            


