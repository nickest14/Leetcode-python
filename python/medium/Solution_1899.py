# 1899. Merge Triplets to Form Target Triplet

from typing import List


class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        ans = set()
        for t in triplets:
            if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
                continue
            for i, v in enumerate(t):
                if v == target[i]:
                    ans.add(i)

        return len(ans) == 3


# triplets = [[2, 5, 3], [1, 8, 4], [1, 7, 5]]
# target = [2, 7, 5]
triplets = [[2,5,8],[9,3,4],[1,2,5],[5,2,3]]
target = [5, 5, 5]
ans = Solution().mergeTriplets(triplets, target)
print(ans)
