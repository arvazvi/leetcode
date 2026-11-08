class Solution:
    def decodeString(self, s: str) -> str:
        def parse(idx: int) -> tuple[str, int]:
            out = ""
            while idx < len(s) and s[idx] != "]":
                if s[idx].isdigit():
                    n = 0
                    while s[idx].isdigit():
                        n = (n * 10) + int(s[idx])
                        idx += 1
                    inner, idx = parse(idx + 1)
                    out += inner * n
                    idx += 1
                else:
                    out += s[idx]
                    idx += 1
            return out, idx
        return parse(0)[0]