# 78. Subsets

from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def dfs(n: int, s: int, cur: list):
            if len(cur) == n:
                ans.append(cur[:])
                return
            else:
                for i in range(s, len(nums)):
                    cur.append(nums[i])
                    dfs(n, i + 1, cur)
                    cur.pop()

        for n in range(len(nums) + 1):
            dfs(n, 0, [])
        return ans


ans = Solution().subsets([1, 2, 3, 4])
print(ans)
