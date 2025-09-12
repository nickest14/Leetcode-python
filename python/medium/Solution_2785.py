# 2785. Sort Vowels in a String


class Solution:
    def sortVowels(self, s: str) -> str:
        vowels_set: set[str] = set("AEIOUaeiou")
        vowels: list[str] = [c for c in s if c in vowels_set]
        vowels.sort()

        ans: list[str] = []
        it: iter[str] = iter(vowels)

        for c in s:
            ans.append(next(it) if c in vowels_set else c)
        return "".join(ans)


ans = Solution().sortVowels("lEetcOde")
print(ans)
