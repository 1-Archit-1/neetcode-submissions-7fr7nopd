# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        dfs =self.dfs(root)
        if isinstance(dfs,bool):
            return False
        else:
            return True
    def dfs(self, node):
        if not node:
            return 0 
        left = self.dfs(node.left)
        if isinstance(left, bool):
            return False
        right = self.dfs(node.right)
        if isinstance(right,bool):
            return False
        if left-right>1 or left-right<-1:
            return False
        else:
            return 1+max(left,right)
