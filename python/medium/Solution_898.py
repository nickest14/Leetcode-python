# 898. Bitwise ORs of Subarrays

from typing import List


class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        ans: set[int] = set()
        cur: set[int] = set()
        for num in arr:
            next_set: set[int] = {num}
            for x in cur:
                next_set.add(x | num)
            cur = next_set
            ans.update(cur)
        return len(ans)


ans = Solution().subarrayBitwiseORs([1, 1, 2])
print(ans)
