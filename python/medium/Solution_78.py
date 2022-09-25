# 78. Subsets


class Solution:

    def subsets(self, nums):

        def dfs(n, s, cur):
            if len(cur) == n:
                ans.append(cur[:])
                return
            for i in range(s, len(nums)):
                cur.append(nums[i])
                dfs(n, i+1, cur)
                cur.pop()
        ans = []
        for i in range(len(nums)+1):
            dfs(i, 0, [])
        return ans


ans = Solution().subsets([1, 2, 3, 4])
print(ans)
