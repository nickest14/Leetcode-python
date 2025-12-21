# 944. Delete Columns to Make Sorted

from typing import List


class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        m, n, ans = len(strs), len(strs[0]), 0
        for j in range(n):
            for i in range(1, m):
                if strs[i][j] < strs[i - 1][j]:
                    ans += 1
                    break
        return ans


ans = Solution().minDeletionSize(["cba", "daf", "ghi"])
print(ans)
