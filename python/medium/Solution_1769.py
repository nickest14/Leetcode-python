# 1769. Minimum Number of Operations to Move All Balls to Each Box

from typing import List


class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n: int = len(boxes)
        ans: list[int] = [0] * n
        prefix_count: int = 0
        prefix_sum: int = 0

        for i in range(n):
            ans[i] = prefix_count * i - prefix_sum
            if boxes[i] == "1":
                prefix_count += 1
                prefix_sum += i

        suffix_count: int = 0
        suffix_sum: int = 0

        for i in range(n - 1, -1, -1):
            ans[i] += suffix_sum - suffix_count * i
            if boxes[i] == "1":
                suffix_count += 1
                suffix_sum += i

        return ans


ans = Solution().minOperations("110")
# ans = Solution().minOperations('11001')
print(ans)
