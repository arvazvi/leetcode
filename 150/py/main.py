class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack: list[int] = []
        for token in tokens:
            if token in "+-*/":
                x, y = stack.pop(), stack.pop()
                if token == "+":
                    stack.append(y + x)
                elif token == "-":
                    stack.append(y - x)
                elif token == "*":
                    stack.append(y * x)
                elif token == "/":
                    stack.append(int(y / x))
            else:
                stack.append(int(token))
        if stack:
            return stack[0]
