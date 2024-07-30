# 1395. Count Number of Teams

from typing import List


class Solution:
    def numTeams(self, rating: List[int]) -> int:
        n: int = len(rating)
        ans: int = 0
        for mid in range(n):
            left_smaller: int = 0
            right_larger: int = 0
            for left in range(mid - 1, -1, -1):
                if rating[left] < rating[mid]:
                    left_smaller += 1

            for right in range(mid + 1, n):
                if rating[right] > rating[mid]:
                    right_larger += 1

            # Calculate and add the number of ascending rating teams (small-mid-large)
            ans += left_smaller * right_larger

            left_larger: int = mid - left_smaller
            right_smaller: int = n - 1 - mid - right_larger
            # Calculate and add the number of descending rating teams (large-mid-small)
            ans += left_larger * right_smaller

        return ans

# class Solution:
#     def numTeams(self, rating: List[int]) -> int:
#         def update(tree, i: int, val: int):
#             while i <= 10 ** 5:
#                 tree[i] += val
#                 i += i & -i

#         def presum(tree, i: int) -> int:
#             total = 0
#             while i > 0:
#                 total += tree[i]
#                 i -= i & -i
#             return total

#         def sufsum(tree, i: int) -> int:
#             return presum(tree, 10**5) - presum(tree, i - 1)

#         before, after, ans = [0] * (10**5 + 1), [0] * (10**5 + 1), 0
#         for rate in rating:
#             update(after, rate, 1)
#         for rate in rating:
#             update(after, rate, -1)
#             ans += presum(before, rate - 1) * sufsum(after, rate + 1)
#             ans += sufsum(before, rate + 1) * presum(after, rate - 1)
#             update(before, rate, 1)
#         return ans


rating = [2, 5, 3, 4, 1]
ans = Solution().numTeams(rating)
print(ans)
