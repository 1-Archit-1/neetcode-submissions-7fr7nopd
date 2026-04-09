class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        l, r = 0 , len(height) -1
        water = 0
        maxl = height[l]
        maxr = height[r]
        while l < r :
            if maxl<maxr:
                l+=1 
                maxl = max(maxl, height[l])
                water+= maxl- height[l]
            else:
                r-=1 
                maxr = max(maxr, height[r])
                water+= maxr-height[r]
        return water
            





