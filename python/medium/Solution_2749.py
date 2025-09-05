# 2749. Minimum Operations to Make the Integer Zero


class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        if num1 == 0:
            return 0

        for t in range(61):
            s: int = num1 - t * num2
            if s < 0:
                continue
            if s < t:
                continue
            ones = s.bit_count()
            if ones <= t:
                return t
        return -1


ans = Solution().makeTheIntegerZero(3, -2)
print(ans)
