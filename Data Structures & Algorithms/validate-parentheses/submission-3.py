from collections import deque 

class Solution:

    def isValid(self, s: str) -> bool:

        if not s:
            return True
        
        mapping = {")":"(","}":"{","]":"["}

        stack = deque()

        for char in s:

            if char in mapping:

                required_mapping = mapping[char]

                if not stack:
                    return False 
                
                if stack[-1]!=required_mapping:
                    return False 
                
                stack.pop()

            else:
                stack.append(char)

        return len(stack)==0

        