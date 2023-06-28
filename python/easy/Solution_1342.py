# 1342. Number of Steps to Reduce a Number to Zero

class Solution:
    def numberOfSteps(self, num: int) -> int:
        steps = num == 0
        while num > 0:
            steps += 1 + (num & 1)
            num >>= 1
        return steps - 1


ans = Solution().numberOfSteps(13)
print(ans)
