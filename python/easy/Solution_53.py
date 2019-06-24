# 53. Maximum Subarray


class Solution:
    def maxSubArray(self, nums) -> int:
        length = len(nums)
        f = [None for _ in range(length+1)]
        f[0] = 0
        for i in range(length):
            f[i+1] = max(f[i]+nums[i], nums[i])
        return max(f[1:])


ans = Solution().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
print(ans)
