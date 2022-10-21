# 1903. Largest Odd Number in String

class Solution:
    def largestOddNumber(self, num: str) -> str:
        for i in reversed(range(len(num))):
            if int(num[i]) % 2 == 1:
                return num[:i + 1]
        return ''


ans = Solution().largestOddNumber('34510')
print(ans)
