# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        return self.diameter(root, 0)[1]
        

    
    def diameter(self, root, maxd):
        if not root:
            return 0, 0
        left_height, maxd_left = self.diameter(root.left, maxd)
        right_height, maxd_right  = self.diameter(root.right, maxd)
        diameter = left_height+right_height
        maxd = max(diameter, maxd_left, maxd_right)
        return 1+max(left_height,right_height), maxd