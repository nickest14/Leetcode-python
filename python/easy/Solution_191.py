# 191. Number of 1 Bits


class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n > 0:
            count += 1
            n &= n - 1
        return count


ans = Solution().hammingWeight('000000111')
print(ans)
