class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        seen2 = set()
        seen = set()
        nums = sorted(nums)
        for i, n in enumerate(nums):
            if n in seen:
                continue
            seen.add(n)
            target = -n 
            l = i + 1
            r = len(nums) - 1 
            while l < r:
                left = nums[l]
                right = nums[r] 
                if left + right == target:
                    x = sorted([left,right,n])
                    check = str(x[0]) + ',' + str(x[1]) + ',' + str(x[2])
                    if check not in seen2:
                        seen2.add(check)
                        res.append(x)
                    l+=1
                    r-=1
                elif left + right < target:
                    l+=1 
                else:
                    r-=1 
                
        return res
