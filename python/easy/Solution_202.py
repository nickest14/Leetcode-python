# 202. Happy Number


class Solution:
    def isHappy(self, n: int) -> bool:
        def sum_value(num: int):
            return sum([int(i)**2 for i in str(num)])

        walker = sum_value(n)
        runner = sum_value(sum_value(n))
        while walker != runner:
            walker = sum_value(walker)
            runner = sum_value(sum_value(runner))
        return walker == 1


ans = Solution().isHappy(19)
# ans = Solution().isHappy(2)
print(ans)
