# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res = [] 
        currq = deque([root])

        while currq:
            newq = deque()
            while currq:
                curr = currq.popleft()
                if curr.left:
                    newq.append(curr.left)
                if curr.right:
                    newq.append(curr.right)
                
            res.append(curr.val)
            currq = newq
        return res 