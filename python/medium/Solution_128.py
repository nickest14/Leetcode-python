# 128. Longest Consecutive Sequence

from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        hash_set = set(nums)
        current_max = 0

        while hash_set:
            num = hash_set.pop()
            high, low = num + 1, num - 1
            while high in hash_set:
                hash_set.remove(high)
                high += 1
            while low in hash_set:
                hash_set.remove(low)
                low -= 1
            current_max = max(current_max, high - low - 1)
        return current_max




ans = Solution().longestConsecutive([100, 4, 200, 1, 3, 2])
print(ans)
