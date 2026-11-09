from collections import Counter


class Solution:
    def countOfAtoms(self, formula: str) -> str:
        n = len(formula)
        idx = 0

        def read_count() -> int:
            nonlocal idx
            start = idx
            while idx < n and formula[idx].isdigit():
                idx += 1
            return int(formula[start:idx]) if idx > start else 1

        stack: list[Counter[str]] = [Counter()]
        while idx < n:
            ch = formula[idx]
            if ch == "(":
                stack.append(Counter())
                idx += 1
            elif ch == ")":
                idx += 1
                mult = read_count()
                top = stack.pop()
                for name, cnt in top.items():
                    stack[-1][name] += cnt * mult
            else:
                start = idx
                idx += 1
                while idx < n and formula[idx].islower():
                    idx += 1
                name = formula[start:idx]
                stack[-1][name] += read_count()

        counts = stack[0]
        return "".join(
            name + (str(counts[name]) if counts[name] > 1 else "")
            for name in sorted(counts)
        )
