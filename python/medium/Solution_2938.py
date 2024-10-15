# 2938. Separate Black and White Balls


class Solution:
    def minimumSteps(self, s: str) -> int:
        black: int = 0
        swap: int = 0
        for c in s:
            if c == '0':
                swap += black
            else:
                black += 1
        return swap


ans = Solution().minimumSteps('00110')
print(ans)
