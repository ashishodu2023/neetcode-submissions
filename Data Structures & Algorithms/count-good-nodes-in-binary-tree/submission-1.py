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

        result =[] 
        def dfs(node:TreeNode,current,maximum):
            if not node:
                return 
            
            if node.val >= maximum:
                current.append(node.val)
            
            dfs(node.left,current,max(maximum,node.val))
            dfs(node.right,current,max(maximum,node.val))

        dfs(root,result,root.val)

        return len(result)
        