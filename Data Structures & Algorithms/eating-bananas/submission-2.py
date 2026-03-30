class Solution:
    def hours_taken(self,k, piles):
        s = 0
        for p in piles:
            s+= p//k 
            if p%k >0: 
                s+=1
        return s 

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1 
        r = max(piles) + 1
        curr = 1 
        while l<=r: 
            mid = l+ (r-l)//2 

            hours = self.hours_taken(mid, piles)
            
            if hours <= h:
                curr = mid
                r = mid-1 
            else:
                l = mid + 1 
        
        return curr 