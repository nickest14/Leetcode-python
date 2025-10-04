# 1518. Water Bottles


class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        ans: int = numBottles

        while numBottles >= numExchange:
            ans += numBottles // numExchange
            numBottles = (numBottles // numExchange) + (numBottles % numExchange)

        return ans


ans = Solution().numWaterBottles(15, 4)
print(ans)
