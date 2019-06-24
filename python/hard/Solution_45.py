# 45. Jump Game II


class Solution:
    def jump(self, nums) -> int:
        length = len(nums)
        if length <= 1:
            return 0
        step = 0
        left, right = 0, 0
        while left <= right:
            temp_right = right
            step += 1
            for i in range(left, right+1):
                new_right = i + nums[i]
                if new_right >= length-1:
                    return step
                if new_right > right:
                    right = new_right

            left = temp_right + 1
        return 0


nums = [4, 1, 2, 1, 3, 1, 1, 2]
ans = Solution().jump(nums)
print(ans)
