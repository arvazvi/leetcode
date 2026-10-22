from typing import List

class Solution:
    def calculate(self, s: str) -> int:
        def tokenize(expression: str) -> List[str]:
            expression = expression.replace(" ", "")
            tokens = []
            i = 0
            n = len(expression)

            while i < n:
                char = expression[i]
                is_unary = char == "-" and (i == 0 or tokens[-1] in "(+-")
                if is_unary:
                    tokens.append("u-")
                    i += 1
                elif char.isdigit():
                    num = [char]
                    i += 1
                    while i < n and expression[i].isdigit():
                        num.append(expression[i])
                        i += 1
                    tokens.append("".join(num))
                else:
                    tokens.append(char)
                    i += 1
            return tokens


        def shunting_yard(tokens: List[str]) -> List[str]:
            output = []
            operators = []

            for token in tokens:
                if token.isdigit():
                    output.append(token)
                elif token == "(":
                    operators.append(token)
                elif token == ")":
                    while operators and operators[-1] != "(":
                        output.append(operators.pop())
                    if operators and operators[-1] == "(":
                        operators.pop()
                elif token == "u-":
                    operators.append(token)
                else:
                    while operators and operators[-1] != "(":
                        output.append(operators.pop())
                    operators.append(token)

            while operators:
                output.append(operators.pop())
            return output

        def rpn(tokens: List[str]):
            stack = []
            for token in tokens:
                if token == "u-":
                    stack.append(-stack.pop())
                elif token in "+-":
                    x, y = stack.pop(), stack.pop()
                    if token == "+":
                        stack.append(y + x)
                    elif token == "-":
                        stack.append(y - x)
                else:
                    stack.append(int(token))
            if stack:
                return stack[0]

        return rpn(shunting_yard(tokenize(s)))