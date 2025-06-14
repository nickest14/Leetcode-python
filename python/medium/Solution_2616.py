# 2616. Minimize the Maximum Difference of Pairs

from typing import List


class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        n: int = len(nums)
        nums.sort()
        low, high = 0, nums[-1] - nums[0]
        while low < high:
            mid = (low + high) // 2
            count: int = 0
            i: int = 1
            while i < n and count < n:
                if nums[i] - nums[i - 1] <= mid:
                    count += 1
                    i += 2
                else:
                    i += 1

            # Binary search update
            if count >= p:
                high = mid
            else:
                low = mid + 1

        # Step 5: Return result
        return low                

ans = Solution().minimizeMax([10, 1, 2, 7, 1, 3], 2)
print(ans)
