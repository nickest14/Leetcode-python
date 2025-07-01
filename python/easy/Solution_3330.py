# 3330. Find the Original Typed String I


class Solution:
    def possibleStringCount(self, word: str) -> int:
        n: int = len(word)
        ans: int = n
        for i in range(1, n):
            if word[i] != word[i - 1]:
                ans -= 1
        return ans


ans = Solution().possibleStringCount("abbcccc")
print(ans)
