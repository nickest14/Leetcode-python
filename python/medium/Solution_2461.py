# 2461. Maximum Sum of Distinct Subarrays With Length K

from typing import List


class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        n: int = len(nums)
        elements = set()
        current_sum: int = 0
        ans: int = 0
        begin: int = 0
        for end in range(n):
            value = nums[end]
            if value not in elements:
                current_sum += value
                elements.add(value)
                if end - begin + 1 == k:
                    if current_sum > ans:
                        ans = current_sum
                    current_sum -= nums[begin]
                    elements.remove(nums[begin])
                    begin += 1
            else:
                while nums[begin] != value:
                    current_sum -= nums[begin]
                    elements.remove(nums[begin])
                    begin += 1
                begin += 1

        return ans


ans = Solution().maximumSubarraySum([1, 5, 4, 2, 9, 9, 9], 3)
print(ans)
