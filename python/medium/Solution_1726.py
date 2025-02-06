# 1726. Tuple with Same Product

from typing import List
from collections import defaultdict


class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        count: dict[int, int] = defaultdict(int)
        ans: int = 0
        for i in range(len(nums)):
            for j in range(i):
                prod: int = nums[i] * nums[j]
                ans += count[prod] * 8
                count[prod] += 1

        return ans


# ans = Solution().tupleSameProduct([2, 3, 4, 6])
# ans = Solution().tupleSameProduct([1,2,8,16])
ans = Solution().tupleSameProduct([1, 2, 4, 5, 10])
print(ans)
