# 3227. Vowels Game in a String


class Solution:
    def doesAliceWin(self, s: str) -> bool:
        vowels: set[str] = set("aeiou")
        even: int = 1
        odd: int = 0
        parity: int = 0

        for c in s:
            if c in vowels:
                parity ^= 1

            if parity == 0:
                even += 1
            else:
                odd += 1

        return even * odd > 0


ans = Solution().doesAliceWin("leetcoder")
print(ans)
