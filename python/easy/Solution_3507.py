# 3507.  Minimum Pair Removal to Sort Array I

from typing import List


class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        def is_increasing(nums: List[int]) -> bool:
            for i in range(len(nums) - 1):
                if nums[i] > nums[i + 1]:
                    return False
            return True

        ans: int = 0
        while not is_increasing(nums):
            min_sum: int = nums[0] + nums[1]
            index: int = 0

            for i in range(1, len(nums) - 1):
                s = nums[i] + nums[i + 1]
                if s < min_sum:
                    min_sum = s
                    index = i

            nums[index] = min_sum
            nums.pop(index + 1)
            ans += 1

        return ans


ans = Solution().minimumPairRemoval([5, 2, 3, 1])
print(ans)
