# 441. Arranging Coins


class Solution:
    def arrangeCoins(self, n: int) -> int:
        left, right = 1, n
        while left < right:
            mid = right - (right - left) // 2
            if (total := mid * (mid + 1) // 2) > n:
                right = mid - 1
            else:
                left = mid
        return left


ans = Solution().arrangeCoins(8)
print(ans)
