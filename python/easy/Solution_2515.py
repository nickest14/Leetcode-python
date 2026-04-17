# 2515. Shortest Distance to Target String in a Circular Array

from typing import List


class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        n: int = len(words)
        for i in range((n >> 1) + 1):
            if (words[(startIndex + i) % n] == target) | (
                words[(startIndex - i) % n] == target
            ):
                return i
        return -1


ans = Solution().closestTarget(["hello", "i", "am", "leetcode", "hello"], "hello", 1)
print(ans)
