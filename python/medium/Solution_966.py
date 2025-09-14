# 966. Vowel Spellchecker


from typing import List


class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:

        def mask_vowels(s: str) -> str:
            return "".join("#" if ch in "aeiou" else ch for ch in s)        

        exact = set(wordlist)
        lower_map: dict[str, str] = {}
        vowel_map: dict[str, str] = {}

        for word in wordlist:
            word_lower = word.lower()
            lower_map.setdefault(word_lower, word)
            word_masked = mask_vowels(word_lower)
            vowel_map.setdefault(word_masked, word)

        ans: list[str] = []
        for query in queries:
            if query in exact:
                ans.append(query)
                continue
            query_lower = query.lower()
            if query_lower in lower_map:
                ans.append(lower_map[query_lower])
                continue
            query_masked = mask_vowels(query_lower)
            ans.append(vowel_map.get(query_masked, ""))
        return ans


wordlist = ["KiTe", "kite", "hare", "Hare"]
queries = [
    "kite",
    "Kite",
    "KiTe",
    "Hare",
    "HARE",
    "Hear",
    "hear",
    "keti",
    "keet",
    "keto",
]
ans = Solution().spellchecker(wordlist, queries)
print(ans)
