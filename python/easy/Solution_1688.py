# 1688. Count of Matches in Tournament


class Solution:
    def numberOfMatches(self, n: int) -> int:
        games = 0
        while n > 1:
            matches = n // 2
            games += matches
            n -= matches
        return games


ans = Solution().numberOfMatches(3)
print(ans)
