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
        
        if  not subRoot:
            return True
        
        return self.isSame(root,subRoot) or self.isSubtree(root.left,subRoot)or self.isSubtree(root.right, subRoot)

    def isSame(self,noder:Optional[TreeNode],nodesub:Optional[TreeNode])->bool:
        if not noder and not nodesub:
            return True
        
        if not noder or not nodesub:
            return False

        if noder.val!=nodesub.val:
            return False 

        return self.isSame(noder.left,nodesub.left) and self.isSame(noder.right,nodesub.right)


        