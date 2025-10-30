# 3370. Smallest Number With All Set Bits


class Solution:
    def smallestNumber(self, n: int) -> int:
        ans: int = 0
        i: int = 0
        while ans < n:
            ans += 1 << i
            i += 1

        return ans


ans = Solution().smallestNumber(5)
print(ans)
