# 2220. Minimum Bit Flips to Convert Number

class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        xor: int = start ^ goal
        return bin(xor).count('1')


ans = Solution().minBitFlips(10, 7)
print(ans)
