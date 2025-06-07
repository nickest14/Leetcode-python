# 2434. Using a Robot to Print the Lexicographically Smallest String

from collections import Counter


class Solution:
    def robotWithString(self, s: str) -> str:
        freq: dict[str, int] = Counter(s)
        ans: list[str] = []
        stack: list[str] = []

        def min_char() -> str:
            for i in range(26):
                ch = chr(ord("a") + i)
                if freq[ch] > 0:
                    return ch
            return ""

        for ch in s:
            stack.append(ch)
            freq[ch] -= 1
            while stack and stack[-1] <= min_char():
                ans.append(stack.pop())
        while stack:
            ans.append(stack.pop())

        return "".join(ans)


# ans = Solution().robotWithString("zza")
ans = Solution().robotWithString("zzzz")
print(ans)
