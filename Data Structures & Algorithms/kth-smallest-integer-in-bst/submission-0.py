# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        if not root or not k:
            return 0
        
        result = []
        def dfs_inorder(node:Optional[TreeNode])->list[int]:
            nonlocal result
            if not node:
                return None 
            
            dfs_inorder(node.left)
            result.append(node.val)
            dfs_inorder(node.right)

            return result 
        
        result=dfs_inorder(root)
        return result[k-1]
            
            
           

        