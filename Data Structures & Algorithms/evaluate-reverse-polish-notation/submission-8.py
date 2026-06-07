from collections import deque


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        if not tokens:
            return 0

        stack = deque()
        operators = set("+-*/")

        for char in tokens:
            if char in operators:
                num2 = stack.pop()
                num1 = stack.pop()

                if char == "+":
                    stack.append(int(num1) + int(num2))
                elif char == "-":
                    stack.append(int(num1) - int(num2))
                elif char == "*":
                    stack.append(int(num1) * int(num2))
                else:
                    stack.append(int(num1/num2))

            else:
                stack.append(int(char))

        return stack[-1]
