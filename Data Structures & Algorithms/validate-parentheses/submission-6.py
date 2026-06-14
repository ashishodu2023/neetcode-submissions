from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:

        if not s:
            return True 
        
        stack = deque()

        brackets = {")":"(","]":"[","}":"{"}

        for char in s:
            if char in brackets:
                required_char = brackets[char]

                if not stack:
                    return False 
            
                if stack[-1]!=required_char:
                    return False 

                stack.pop()
            else:
                stack.append(char)

        return len(stack) ==0
            
            