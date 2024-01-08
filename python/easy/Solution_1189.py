# 1189. Maximum Number of Balloons

from collections import Counter


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        count_text = Counter(text)
        balloon = Counter('balloon')
        ans = len(text)
        for c in balloon:
            ans = min(ans, count_text[c] // balloon[c])
        return ans


ans = Solution().maxNumberOfBalloons("loonbalxballpoon")
print(ans)
