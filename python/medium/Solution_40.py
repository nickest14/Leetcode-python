# 40. Combination Sum II

from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        candidates.sort()

        def dfs(idx: int, path: list[int], cur: int):
            if cur > target:
                return
            if cur == target:
                ans.append(path)
            for i in range(idx, len(candidates)):
                if i > idx and candidates[i] == candidates[i - 1]:
                    continue
                dfs(i + 1, path + [candidates[i]], cur + candidates[i])

        dfs(0, [], 0)

        return ans


# ans = Solution().combinationSum2([10, 1, 2, 7, 6, 1, 5], 8)
ans = Solution().combinationSum2([1,1,1,1,2], 3)
print(ans)
