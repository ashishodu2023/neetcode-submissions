# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Inorder = "left,root,right"
# preorder = "root,left,right"


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        if not preorder or not inorder:
            return None 
        
        seen_inorder = dict()
        self.index_in_preorder = 0 

        for index,value in enumerate(inorder):
            seen_inorder[value] = index

        
        def dfs(left, right):
            if left > right:
                return None

            root_val = preorder[self.index_in_preorder]
            self.index_in_preorder+=1
            root = TreeNode(root_val)

            root_in_inorder = seen_inorder[root_val]

            root.left = dfs(left,root_in_inorder -1)
            root.right = dfs(root_in_inorder+1,right)

            return root 

        return dfs(0,len(inorder) - 1)

        


            


        