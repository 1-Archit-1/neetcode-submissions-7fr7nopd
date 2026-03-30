class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0 
        x = set(nums)
        res = -sys.maxsize
        for n in nums:
            if n-1 in x:
                continue 
            length = 1
            z= n  
            while True:
                z=z+1
                if z in x:
                    length+=1 
                else:
                    break
            res = max(res,length)
        return res 