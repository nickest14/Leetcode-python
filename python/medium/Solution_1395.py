# 1395. Count Number of Teams

from typing import List


class Solution:
    def numTeams(self, rating: List[int]) -> int:
        def update(tree, i: int, val: int):
            while i <= 10 ** 5:
                tree[i] += val
                i += i & -i

        def presum(tree, i: int) -> int:
            total = 0
            while i > 0:
                total += tree[i]
                i -= i & -i
            return total

        def sufsum(tree, i: int) -> int:
            return presum(tree, 10**5) - presum(tree, i - 1)

        before, after, ans = [0] * (10**5 + 1), [0] * (10**5 + 1), 0
        for rate in rating:
            update(after, rate, 1)
        for rate in rating:
            update(after, rate, -1)
            ans += presum(before, rate - 1) * sufsum(after, rate + 1)
            ans += sufsum(before, rate + 1) * presum(after, rate - 1)
            update(before, rate, 1)
        return ans


# class Solution:
#     def numTeams(self, rating: List[int]) -> int:
#         ans = 0
#         for i, ri in enumerate(rating):
#             left_big, right_big = 0,  0
#             left_small, right_small = 0,  0
#             for j, rj in enumerate(rating):
#                 if i > j:
#                     if ri > rj:
#                         left_small += 1
#                     else:
#                         left_big += 1
#                 elif i < j:
#                     if ri > rj:
#                         right_small += 1
#                     else:
#                         right_big += 1
#             ans += (left_small * right_big + left_big * right_small)
#         return ans


rating = [2, 5, 3, 4, 1]
ans = Solution().numTeams(rating)
print(ans)
