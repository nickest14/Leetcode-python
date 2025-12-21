# 955. Delete Columns to Make Sorted II

from typing import List


class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n: int = len(strs)
        m: int = len(strs[0])

        resolved: list[bool] = [False] * (n - 1)
        unresolved: int = n - 1
        deletions: int = 0

        for col in range(m):
            if unresolved == 0:
                break

            bad = False
            for i in range(n - 1):
                if not resolved[i] and strs[i][col] > strs[i + 1][col]:
                    bad = True
                    break

            if bad:
                deletions += 1
                continue

            for i in range(n - 1):
                if not resolved[i] and strs[i][col] < strs[i + 1][col]:
                    resolved[i] = True
                    unresolved -= 1

        return deletions        


ans = Solution().minDeletionSize(["ca", "bb", "ac"])
print(ans)
