# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        if root is None:
            return root
        
        currq = deque([root])
        while currq:
            newq = deque() 
            while currq:
                curr = currq.popleft()
                temp = curr.left
                curr.left = curr.right
                curr.right = temp
                if curr.left:
                    newq.append(curr.left)
                if curr.right:
                    newq.append(curr.right)
            currq = newq
        return root
                

             
                
        

