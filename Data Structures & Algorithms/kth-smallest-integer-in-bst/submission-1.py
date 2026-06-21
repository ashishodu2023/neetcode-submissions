# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        if not root:
            return 0 
        
        self.smallest_value = 0 
        self.count = 0 

        def dfs(node):
            if not node:
                return 0
            dfs(node.left)

            self.count+=1
            if self.count == k:
                self.smallest_value = node.val 
                return 
            
            dfs(node.right)
        
        dfs(root)
        return self.smallest_value 

            

