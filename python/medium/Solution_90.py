# 90. Subsets II


class Solution:
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
