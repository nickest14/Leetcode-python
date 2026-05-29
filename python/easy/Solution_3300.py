# 3300. Minimum Element After Replacement With Digit Sum

from typing import List


class Solution:
    def minElement(self, nums: List[int]) -> int:
        def digit_sum(n: int):
            total: int = 0
            while n > 0:
                total += n % 10
                n //= 10
            return total
        
        return min(digit_sum(num) for num in nums)        


ans = Solution().minElement([10,12,13,14])
print(ans)
