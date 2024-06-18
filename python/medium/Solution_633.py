# 633. Sum of Square Numbers


class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        start = 0
        end = int(c ** 0.5)
        while start <= end:
            sum = start ** 2 + end ** 2
            if sum == c:
                return True
            elif sum > c:
                end -= 1
            else:
                start += 1

        return False


ans = Solution().judgeSquareSum(34)
# ans = Solution().judgeSquareSum(4)
print(ans)
