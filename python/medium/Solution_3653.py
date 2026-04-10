# 3653. XOR After Range Multiplication Queries I

from typing import List


class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        mod: int = 10**9 + 7

        for query in queries:
            left = query[0]
            right = query[1]
            k = query[2]
            v = query[3]

            idx = left
            while idx <= right:
                temp = nums[idx]
                nums[idx] = (temp * v) % mod
                idx += k

        ans: int = 0
        for num in nums:
            ans ^= num

        return ans


ans = Solution().xorAfterQueries([1, 1, 1], [[0, 2, 1, 4]])
print(ans)
