# 179. Largest Number

from typing import List


class Sort(str):
    def __lt__(self, other):
        return self + other < other + self


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        strs = ''.join(sorted(map(str, nums), key=Sort, reverse=True))
        return strs if strs[0] != '0' else '0'


ans = Solution().largestNumber([3, 30, 34, 5, 9])
print(ans)
