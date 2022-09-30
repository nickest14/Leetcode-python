# 421. Maximum XOR of Two Numbers in an Array


from typing import List

import collections


class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        ans = -1
        trie = {}
        length = max(nums).bit_length()
        for num in nums:
            curr = opposite = trie
            binary = f'{num:b}'.zfill(length)
            for c in binary:
                curr = curr.setdefault(c, {})
                opposite = opposite.get(str(1 - int(c))) or opposite.get(c)
            curr['$'] = num
            ans = max(ans, num ^ opposite['$'])
        return ans


# Brute-force
# class Solution:
#     def findMaximumXOR(self, nums: List[int]) -> int:
#         ans = -1
#         for ind, i in enumerate(nums):
#             for j in nums[ind+1:]:
#                 print(f'{i=} {j=}')
#                 if (value := i ^ j) and value > ans:
#                     ans = value
#         return ans


ans = Solution().findMaximumXOR([3, 10, 5, 25, 2, 8])
print(ans)
