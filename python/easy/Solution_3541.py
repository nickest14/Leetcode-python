# 3541. Find Most Frequent Vowel and Consonant

from collections import Counter


class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowels: set[str] = set("aeiou")
        freq: Counter = Counter(s)

        vowel_counts = [freq[vowel] for vowel in vowels]
        max_vowel: int = max(vowel_counts) if vowel_counts else 0
        
        consonant_counts = [count for key, count in freq.items() if key not in vowels]
        max_consonant: int = max(consonant_counts) if consonant_counts else 0
        
        return max_vowel + max_consonant


ans = Solution().maxFreqSum("successes")
# ans = Solution().maxFreqSum("aeiaeia")
print(ans)
