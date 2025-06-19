# 2966. Divide Array Into Arrays With Max Difference

from typing import List


class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        n: int = len(nums)

        ans: List[List[int]] = []
        for i in range(0, n, 3):
            if i+2 >= n or nums[i+2] - nums[i] > k:
                return []
            ans.append(nums[i: i+3])
        return ans

ans = Solution().divideArray([1,3,4,8,7,9,3,5,1], 2)
print(ans)
