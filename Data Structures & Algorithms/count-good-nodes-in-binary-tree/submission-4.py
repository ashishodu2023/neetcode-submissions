# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        if not root:
            return False

        def dfs(node, max_so_far) -> int:

            if not node:
                return 0

            good_node = 1 if node.val >= max_so_far else 0
            max_so_far = max(max_so_far, node.val)

            return good_node + dfs(node.left, max_so_far) + dfs(node.right, max_so_far)


        return dfs(root,root.val)
