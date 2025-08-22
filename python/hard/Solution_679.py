# 679. 24 Game

from typing import List


class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        eps: float = 1e-6

        def dfs(nums: List[float]) -> bool:
            if len(nums) == 1:
                return abs(nums[0] - 24.0) < eps

            for i in range(len(nums)):
                for j in range(len(nums)):
                    if i == j:
                        continue
                    next_nums = [nums[k] for k in range(len(nums)) if k != i and k != j]
                    a, b = nums[i], nums[j]
                    candidates = [a + b, a - b, b - a, a * b]
                    if abs(b) > eps:
                        candidates.append(a / b)
                    if abs(a) > eps:
                        candidates.append(b / a)

                    for val in candidates:
                        if dfs(next_nums + [val]):
                            return True
            return False

        return dfs([float(x) for x in cards])


ans = Solution().judgePoint24([4, 1, 8, 7])
print(ans)
