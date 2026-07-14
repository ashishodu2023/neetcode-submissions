class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if not tokens:
            return 0

        stack = []
        operators = set("+-*/")

        for token in tokens:
            if token in operators:
                num2 = stack.pop()
                num1 = stack.pop()

                if token == "+":
                    stack.append(int(num1) + int(num2))
                elif token == "-":
                    stack.append(int(num1) - int(num2))
                elif token == "*":
                    stack.append(int(num1) * int(num2))
                else:
                    stack.append(int(num1 / num2))

            else:
                stack.append(int(token))

        return stack[-1]
