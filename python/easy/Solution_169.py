# 169. Majority Element


from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority, count = None, 0
        for num in nums:
            if count == 0:
                majority = num
            count += 1 if num == majority else -1
            print(f'{majority=} {count=}')
        return majority


ans = Solution().majorityElement([1, 2, 2, 1, 2, 1, 1])
print(ans)
