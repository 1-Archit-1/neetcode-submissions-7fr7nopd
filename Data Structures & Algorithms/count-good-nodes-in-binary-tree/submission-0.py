# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import sys
class Solution:
    
    def goodNodes(self, root: TreeNode) -> int:
        self.count=0
        self.curr_path = [root]
        self.dfs(root)
        
        return self.count
    def dfs(self, node):

        if not node:
            return None
        if node.val>=self.curr_path[-1].val:
            self.curr_path.append(node)
            self.count+=1
        self.dfs(node.left)
        self.dfs(node.right)
        if node==self.curr_path[-1]:
            self.curr_path=self.curr_path[:-1]
        