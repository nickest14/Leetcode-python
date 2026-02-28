# 1404. Number of Steps to Reduce a Number in Binary Representation to One


class Solution:
    def numSteps(self, s: str) -> int:
        steps: int = 0
        carry: int = 0
        for i in range(len(s) - 1, 0, -1):
            if ((s[i] == "1") + carry) & 1:
                steps += 2
                carry = 1
            else:
                steps += 1

        return steps + carry


ans = Solution().numSteps("1101")
print(ans)
