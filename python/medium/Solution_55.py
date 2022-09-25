# 55. Jump Game


class Solution:
    def canJump(self, nums) -> bool:
        right = 0
        last_index = len(nums) - 1
        for i in range(len(nums)):
            if i > right:
                return False
            steps = nums[i]
            right = (steps + i) if (steps + i) > right else right
            if right >= last_index:
                return True
        return False


ans = Solution().canJump([1, 1, 1, 2, 0, 5])
# ans = Solution().canJump([0])
print(ans)
