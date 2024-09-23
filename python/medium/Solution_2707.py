# 2707. Extra Characters in a String

from typing import List


class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        max_val: int = len(s) + 1
        dp: list[int] = [max_val] * (len(s) + 1)
        dp[0] = 0
        dic_set = set(dictionary)

        for i in range(1, len(s) + 1):
            dp[i] = dp[i - 1] + 1
            for j in range(1, i + 1):
                if s[i - j: i] in dic_set:
                    dp[i] = min(dp[i], dp[i - j])
        return dp[-1]


ans = Solution().minExtraChar('leetscode', ['leet', 'code', 'leetcode'])
print(ans)
