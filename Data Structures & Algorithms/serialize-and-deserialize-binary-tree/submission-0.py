# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""

        result = [] 
        def dfs_preorder(node:Optional[TreeNode]) ->str:
            if not node:
                result.append('N')
                return 
            result.append(str(node.val))
            dfs_preorder(node.left)
            dfs_preorder(node.right)

        dfs_preorder(root)
        return ",".join(result) 
                

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None

        vals = iter(data.split(","))

        def dfs():
            val = next(vals)
            if val == 'N':
                return None
            node = TreeNode(int(val))
            node.left = dfs()
            node.right = dfs()
            return node

        return dfs()
