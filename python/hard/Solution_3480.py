# 3480. Maximize Subarrays After Removing One Conflicting Pair

from typing import List


class Solution:
    def maxSubarrays(self, n: int, conflictingPairs: List[List[int]]) -> int:
        right: list[list[int]] = [[] for _ in range(n + 1)]
        for a, b in conflictingPairs:
            right[max(a, b)].append(min(a, b))

        ans: int = 0
        left: list[int] = [0, 0]
        bonus: list[int] = [0] * (n + 1)
        
        for r in range(1, n + 1):
            for l in right[r]:
                if l > left[0]:
                    left = [l, left[0]]
                elif l > left[1]:
                    left = [left[0], l]
            
            ans += r - left[0]

            if left[0] > 0:
                bonus[left[0]] += left[0] - left[1]
        
        return ans + max(bonus)


ans = Solution().maxSubarrays(4, [[2, 3], [1, 4]])
print(ans)
