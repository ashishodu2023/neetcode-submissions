from collections import deque


class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return True

        bracket_map = {")": "(", "}": "{", "]": "["}

        stack = deque()

        for char in s:
            if char in bracket_map:
                required_char = bracket_map[char]

                if not stack:
                    return False 
                if stack[-1]!=required_char:
                    return False 
                
                stack.pop()
            else:
                stack.append(char)

        return len(stack)==0
                
