# 2131. Longest Palindrome by Concatenating Two Letter Words

from collections import Counter
from typing import List


class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        freq: Counter = Counter(words)
        palindrome_length: int = 0
        has_center_word: bool = False

        for word, count in freq.items():
            if word[0] == word[1]:
                palindrome_length += count // 2 * 4
                if count & 1:
                    has_center_word = True
            elif word[0] < word[1]:
                reverse_word: str = word[1] + word[0]
                palindrome_length += min(count, freq[reverse_word]) * 4

        return palindrome_length + has_center_word * 2


ans = Solution().longestPalindrome(["lc", "cl", "gg"])
print(ans)
