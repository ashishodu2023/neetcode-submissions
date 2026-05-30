# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def dfs(nodep: Optional[TreeNode], nodeq: Optional[TreeNode]):
            if  not nodep and  not nodeq:
                return True
            if not nodeq or not nodep:
                return False
            if nodep.val!=nodeq.val:
                return False 
            return dfs(nodep.left, nodeq.left) and dfs(nodep.right, nodeq.right)

        return dfs(p,q)

        