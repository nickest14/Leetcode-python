# 960. Delete Columns to Make Sorted III

from typing import List


class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        m: int = len(strs[0])
        dp: list[int] = [1] * m

        for i in range(m):
            for j in range(i):
                if all(row[j] <= row[i] for row in strs):
                    dp[i] = max(dp[i], dp[j] + 1)

        return m - max(dp)


ans = Solution().minDeletionSize(["babca", "bbazb"])
print(ans)
