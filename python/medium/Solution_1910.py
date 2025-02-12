# 1910. Remove All Occurrences of a Substring


class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        stack: list[str] = []
        n: int = len(part)

        def _check():
            return "".join(stack[-n:]) == part

        for c in s:
            stack.append(c)
            if len(stack) >= n and _check():
                for _ in range(n):
                    stack.pop()

        return "".join(stack)


ans = Solution().removeOccurrences("daabcbaabcbc", "abc")
print(ans)
