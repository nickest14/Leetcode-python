# 1422. Maximum Score After Splitting a String


class Solution:
    def maxScore(self, s: str) -> int:
        zeros, ones, score = 0, 0, float('-inf')
        for val in s[:-1]:
            if val == '1':
                ones += 1
            else:
                zeros += 1
            score = max(score, zeros - ones)
        return score + ones + (s[-1] == '1')


# ans = Solution().maxScore('011101')
ans = Solution().maxScore('111000')
print(ans)
