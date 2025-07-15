# 3136. Valid Word


class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3:
            return False
        vowels: list[str] = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
        v: int = 0
        c: int = 0
        for ch in word:
            if ch.isdigit():
                continue
            if ch.isalpha():
                 (v := v + 1) if ch in vowels else (c := c + 1)
            else:
                return False

        return v > 0 and c > 0


ans = Solution().isValid("234Adas")
print(ans)
