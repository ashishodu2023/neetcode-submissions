# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0 
        
        max_path_sum = float('-inf')
        def dfs(node: Optional[TreeNode])->int:

            if not node:
                return 0 
            nonlocal max_path_sum 

            left_sum = max(0,dfs(node.left))
            right_sum = max(0,dfs(node.right))

            current_sum = left_sum + right_sum
            max_path_sum = max(max_path_sum, node.val + left_sum + right_sum)

            return node.val + max(left_sum, right_sum)
        
        dfs(root)
        return max_path_sum

        