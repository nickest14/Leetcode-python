# 1371. Find the Longest Substring Containing Vowels in Even Counts


class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        vowels: dict[str, int] = {'a': 1, 'e': 2, 'i': 4, 'o': 8, 'u': 16}
        dic: dict[int, int] = {0: -1}
        value: int = 0
        ans: int = 0
        for i, c in enumerate(s):
            if c in vowels:
                value ^= vowels[c]
            if value not in dic:
                dic[value] = i
            else:
                ans = max(ans, i - dic[value])
        return ans


ans = Solution().findTheLongestSubstring('eleetminicoworoep')
# ans = Solution().findTheLongestSubstring('aqqaa')
print(ans)
