from collections import deque
from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if not tokens:
            return 0

        stack = deque()
        operators = set("+-*/")

        for chars in tokens:
            if chars not in operators:        
                stack.append(int(chars))
            else:                            
                num2 = stack.pop()
                num1 = stack.pop()

                if chars == "+":
                    stack.append(num1 + num2)
                elif chars == "-":
                    stack.append(num1 - num2)
                elif chars == "*":
                    stack.append(num1 * num2)
                else:
                    stack.append(int(num1 / num2))  

        return stack[-1]