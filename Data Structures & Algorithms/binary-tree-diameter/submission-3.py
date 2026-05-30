class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = 0

        def dfs(node: Optional[TreeNode]) -> int:
            nonlocal ans
            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            ans = max(ans, left + right)      # diameter through this node
            return 1 + max(left, right)       # height

        dfs(root)
        return ans