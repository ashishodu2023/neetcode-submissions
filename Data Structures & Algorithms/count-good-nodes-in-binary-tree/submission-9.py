# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0 

        def count_node(node,max_so_far):
            if not node:
                return 0 
            count = 1 if node.val>=max_so_far else 0 
            new_count = max(max_so_far,node.val)
            count+=count_node(node.left,new_count)
            count+=count_node(node.right,new_count)

            return count 
        
        return count_node(root,root.val)
        