# 1935. Maximum Number of Words You Can Type


class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        brokenLetters: set[str] = set(brokenLetters)
        words: list[str] = text.split()
        ans: int = 0
        for word in words:
            if not any(letter in brokenLetters for letter in word):
                ans += 1
        return ans


ans = Solution().canBeTypedWords('hello world', 'ad')
print(ans)
