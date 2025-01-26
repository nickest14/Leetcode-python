# 2948. Make Lexicographically Smallest Array by Swapping Elements

from typing import List


class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        pairs: list[tuple[int, int]] = [
            (val, i) for i, val in enumerate(nums)
        ]  # (value, index)
        pairs.sort(key=lambda x: x[0])
        values, indices = [[] for _ in range(len(nums))], [[] for _ in range(len(nums))]

        group_idx, current_val = 0, pairs[0][0]
        values[group_idx].append(pairs[0][0])
        indices[group_idx].append(pairs[0][1])
        for i in range(1, len(nums)):
            if pairs[i][0] - current_val > limit:
                group_idx += 1
            values[group_idx].append(pairs[i][0])
            indices[group_idx].append(pairs[i][1])
            current_val = pairs[i][0]

        for i in range(len(nums)):
            indices[i].sort()

        ans = [0] * len(nums)
        for i in range(len(nums)):
            for j in range(len(values[i])):
                ans[indices[i][j]] = values[i][j]

        return ans


ans = Solution().lexicographicallySmallestArray([1, 5, 3, 9, 8], 2)
# ans = Solution().lexicographicallySmallestArray([1, 7, 6, 18, 2, 1], 3)
print(ans)
