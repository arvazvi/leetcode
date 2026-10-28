class Solution:
    def calculate(self, s: str) -> int:
        def tokenize(expression: str) -> list[str]:
            expression = expression.replace(" ", "")
            tokens: list[str] = []
            i = 0
            n = len(expression)

            while i < n:
                char = expression[i]
                if char.isdigit():
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


        def shunting_yard(tokens: list[str]) -> list[str]:
            output: list[str] = []
            operators: list[str] = []
            precedence: dict[str, int] = {"+": 1, "-": 1, "*": 2, "/": 2}

            for token in tokens:
                if token.isdigit() or token == "(":
                    output.append(token)
                elif token == ")":
                    while operators and operators[-1] != "(":
                        output.append(operators.pop())
                    if operators and operators[-1] == "(":
                        operators.pop()
                else:
                    while (
                        operators and operators[-1] != "(" and
                        (
                            precedence[operators[-1]] > precedence[token] or 
                            (precedence[operators[-1]] == precedence[token] and token in "+*-/")
                        )
                    ):
                        output.append(operators.pop())
                    operators.append(token)

            while operators:
                output.append(operators.pop())
            return output

        def RPN(tokens: list[str]) -> int | None:
            stack: list[int] = []
            for token in tokens:
                if token in "+-/*":
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

        return RPN(shunting_yard(tokenize(s)))
