# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False

        if self.sameTree(root, subRoot):
            return True
        leftIsSame = self.isSubtree(root.left, subRoot)
        rightIsSame = self.isSubtree(root.right, subRoot)

        return leftIsSame or rightIsSame

    def sameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True

        if not p or not q:
            return False

        if p.val != q.val:
            return False

        leftSame = self.sameTree(p.left, q.left)
        rightSame = self.sameTree(p.right, q.right)

        return leftSame and rightSame
