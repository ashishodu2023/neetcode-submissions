"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:

        if not root:
            return []
        result = []
        
        def dfs(node)->List[int]:
            if not node:
                return []

            for child in node.children:
                dfs(child)
            result.append(node.val)

            return result

        return dfs(root)

            
        