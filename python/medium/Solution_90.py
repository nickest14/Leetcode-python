# 90. Subsets II

from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()

        def backtrack(i, subset):
            if len(nums) == i:
                ans.append(subset[::])
                return

            # All subsets that include nums[i]
            subset.append(nums[i])
            backtrack(i + 1, subset)
            subset.pop()

            # All subsets that don't include nums[i]
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            backtrack(i + 1, subset)

        backtrack(0, [])
        return ans


class Solution2:
    def dfs(self, nums, index, res, path):
        if path not in res:
            res.append(path)
        for i in range(index, len(nums)):
            if i > index and nums[i] == nums[i - 1]:
                continue
            self.dfs(nums, i + 1, res, path + [nums[i]])

    def subsetsWithDup(self, nums):
        ans = []
        nums.sort()
        self.dfs(nums, 0, ans, [])
        return ans

    def subsetsWithDup_2(self, nums):
        ans = []

        def innerdfs(n, index, path):
            if len(path) == n:
                if path not in ans:
                    ans.append(path[:])
                return
            for i in range(index, len(nums)):
                path.append(nums[i])
                innerdfs(n, i+1, path)
                path.pop()
        nums.sort()
        for n in range(len(nums)+1):
            innerdfs(n, 0, [])
        return ans


ans = Solution().subsetsWithDup([1, 2, 2, 3])
print(ans)
