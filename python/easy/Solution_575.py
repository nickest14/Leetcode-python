# 575. Distribute Candies

from typing import List


class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        return min(len(set(candyType)), len(candyType) // 2)


# Another solution
# class Solution:
#     def distributeCandies(self, candyType: List[int]) -> int:
#         candyType.sort()
#         unique = sum(candyType[i] != candyType[i-1] for i, c in enumerate(candyType))
#         return min(len(candyType) // 2, unique + (candyType[0] == candyType[-1]))


ans = Solution().distributeCandies([1, 2, 3, 4, 5, 5, 5, 5])
print(ans)
