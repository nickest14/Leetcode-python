# 1968. Array With Elements Not Equal to Average of Neighbors

from typing import List


class Solution:
    # Input: nums = [5, 4, 3, 2, 1]
    # Sorted nums = [1, 2, 3, 4, 5]
    # 1st Filled arr = [1,_,2,_,3]
    # 2nd Filled arr = [1, 4, 2, 3, 5]
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        i, j, n = 0, 0, len(nums)
        ans = [0] * n

        while i < n and j < n:
            ans[i] = nums[j]
            i = i + 2
            j = j + 1

        i = 1
        while i < n and j < n:
            ans[i] = nums[j]
            i = i + 2
            j = j + 1

        return ans


ans = Solution().rearrangeArray([5, 4, 3, 2, 1])
print(ans)
