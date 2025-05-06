# 1920. Build Array from Permutation


from typing import List


class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        return [nums[num] for num in nums]


ans = Solution().buildArray([0, 2, 1, 5, 3, 4])
print(ans)
