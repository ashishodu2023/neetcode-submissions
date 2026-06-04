from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:

        if not s:
            return True

        mapping_chars = {')':'(','}':'{',']':'['}

        stack = deque()

        for char in s:

            if char in mapping_chars:

                required_opening = mapping_chars[char]

                if not stack:
                    return False 

                if stack[-1]!=required_opening:
                    return False 
            
                stack.pop()

            else:
                stack.append(char)

        
        return len(stack)==0



        
        