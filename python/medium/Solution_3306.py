# 3306. Count of Substrings Containing Every Vowel and K Consonants II

from collections import defaultdict


class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        vowels: str = "aeiou"

        def atleast_k_consonants(k: int) -> int:
            vowels_in_window: dict[str, int] = defaultdict(int)
            left: int = 0
            consonants: int = 0
            count: int = 0
            for right, char in enumerate(word):
                if char in vowels:
                    vowels_in_window[char] += 1
                else:
                    consonants += 1

                while consonants >= k and len(vowels_in_window) == 5:
                    count += len(word) - right
                    if word[left] in vowels:
                        vowels_in_window[word[left]] -= 1
                        if vowels_in_window[word[left]] == 0:
                            del vowels_in_window[word[left]]
                    else:
                        consonants -= 1
                    left += 1
            return count

        return atleast_k_consonants(k) - atleast_k_consonants(k + 1)


ans = Solution().countOfSubstrings("xxxaeiou", 1)
# ans = Solution().countOfSubstrings("xaeiouzy", 1)
# ans = Solution().countOfSubstrings("ieaouqqieaouqq", 1)

print(ans)
