# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.isBalanced = True 

        def height(root):
            if not self.isBalanced :
                return 0 
            if not root:
                return 0
            left_height = height(root.left)
            right_height = height(root.right)
            diff = abs(left_height-right_height)
            if diff>1:
                self.isBalanced = False 
                return 0 
            return 1+max(left_height, right_height)
        
        height(root)
        return self.isBalanced
        
