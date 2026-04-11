class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        stack = [] 
        maxarea = 0 
        for i in range(len(heights)): 
            start = i 
            while stack and stack[-1][1] > heights[i]:
                start, sh = stack.pop()
                maxarea = max(maxarea, (i-start) *sh)
            stack.append((start, heights[i]))
        
        for start, h in stack:
            maxarea = max(maxarea, (len(heights) - start) *h)
        
        return maxarea 
    

        