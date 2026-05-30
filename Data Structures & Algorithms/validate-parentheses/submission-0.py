from collections import deque 

class Solution:
    def isValid(self, s: str) -> bool:
        
        if not s:
            return False 
        
        stack = deque()
        matches = {')': '(', '}': '{', ']': '['}

        for char in s:
            if char in matches:
                if not stack or stack[-1] != matches[char]:
                    return False 
                stack.pop()
            else:
                stack.append(char)
        return len(stack) == 0  

        