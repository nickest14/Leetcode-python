# 557. Reverse Words in a String III


class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(word[::-1] for word in s.split())


ans = Solution().reverseWords("Let's take LeetCode contest")
print(ans)
