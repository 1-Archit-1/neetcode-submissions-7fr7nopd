class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.bs(nums,target, 0, len(nums)-1)
    def bs(self,nums,target,start,end):
        check = (end+start)//2
        print(start,end)
        if nums[check] == target:
            return check
        elif end-start<1:
            return -1
        elif nums[check]>target:
            return self.bs(nums,target, start, check-1)
        else:
            return self.bs(nums,target,check+1,end)
    