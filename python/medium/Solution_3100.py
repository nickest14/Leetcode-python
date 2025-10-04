# 3100. Water Bottles II


class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        ans: int = numBottles
        empty_bottles: int = numBottles

        while empty_bottles >= numExchange:
            empty_bottles -= numExchange
            numExchange += 1
            ans += 1
            empty_bottles += 1
        return ans


ans = Solution().maxBottlesDrunk(13, 6)
print(ans)
