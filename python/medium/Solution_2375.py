# 2375. Construct Smallest Number From DI String


class Solution:
    def smallestNumber(self, pattern: str) -> str:
        n: int = len(pattern)
        s: list[str] = []
        stack: list[str] = []

        for i in range(n + 1):
            stack.append(str(i + 1))
            if i == n or pattern[i] == "I":
                while stack:
                    s.append(stack.pop())

        return "".join(s)


ans = Solution().smallestNumber("IIIDIDDD")
print(ans)
