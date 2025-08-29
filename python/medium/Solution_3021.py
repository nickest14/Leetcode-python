# 3021. Alice and Bob Playing Flower Game


class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        return n * m // 2


ans = Solution().flowerGame(3, 2)

print(ans)
