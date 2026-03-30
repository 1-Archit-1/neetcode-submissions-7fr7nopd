class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l =0 
        r = len(heights) - 1 
        curr = min(heights[l], heights[r]) * (r-l)
        currl = heights[l]
        currr = heights[r]
        update = 0 
        while l < r: 
            if (heights[l]>=heights[r]):
                r-=1
            else:
                l+=1
            new = min(heights[l], heights[r]) * (r-l)
            if new > curr:
                curr = new
        return curr 
