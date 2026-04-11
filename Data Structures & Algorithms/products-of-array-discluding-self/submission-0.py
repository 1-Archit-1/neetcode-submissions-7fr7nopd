class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_sum = [None] * len(nums)
        prefix_sum[0] = 1   

        zero_count = 0 
        idx_zero = -1 
        if nums[0] == 0:
            zero_count+=1 
            idx_zero = 0 
        for i in range(1, len(nums)):
            if nums[i] == 0:
                zero_count+=1
                if zero_count == 2:
                    return [0] * len(nums)
                else:
                    idx_zero = i 
            prefix_sum[i] = prefix_sum[i-1] * nums[i-1] 
        
        if zero_count == 1:
            x = 1
            for i in nums:
                x*=i
            res =[0] * len(nums)
            res[idx_zero] = x

        
        suffix_sum = [None] * len(nums)
        suffix_sum[-1] = 1

        for i in range(len(nums)-2,-1,-1): 
            suffix_sum[i] = suffix_sum[i+1] * nums[i+1]
        res =[] 
        for i in range(len(nums)):
            res.append(prefix_sum[i] * suffix_sum[i])

        return res        


