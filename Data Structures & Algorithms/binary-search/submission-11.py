class Solution:

    def binary_search(self, nums , left, right, target):
        if right<left:
            return -1 
        mid = (left+right)//2
        if nums[mid] == target:
            return mid
        elif nums[mid] <target:
            left = mid+1 
            right = right 
            return self.binary_search(nums, left,right,target)
        else:
            left = left
            right = mid - 1 
            return self.binary_search(nums, left,right,target)

    def search(self, nums: List[int], target: int) -> int:
        left = 0 
        right = len(nums) - 1
        return self.binary_search(nums, left,right,target)