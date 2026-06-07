from collections import deque
class Solution:


    def isValid(self, s: str) -> bool:

        if not s:
            return True
        
        bracket = {')':'(','}':'{',']':'['}
        stack = deque()

        for char in s:
            if char in bracket:

                required_mapping = bracket[char]

                if not stack:
                    return False 
                
                if stack[-1]!=required_mapping:
                    return False 
                
                stack.pop()

            else:
                stack.append(char)

        return len(stack)==0

        