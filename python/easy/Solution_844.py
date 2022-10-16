# 844. Backspace String Compare


class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def build(string: str) -> list:
            stack = []
            for s in string:
                if s != '#':
                    stack.append(s)
                elif stack:
                    stack.pop()
            return stack
        return build(s) == build(t)


ans = Solution().backspaceCompare('y#fo##f', 'y#f#o##f')
print(ans)
