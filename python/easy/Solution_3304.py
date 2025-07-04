# 3304. Find the K-th Character in String Game I

class Solution:
    def kthCharacter(self, k: int) -> str:
        word: list[str] = ['a']
        while len(word) < k:
            size: int = len(word)
            for i in range(size):
                next_char = chr(ord('a') + ((ord(word[i]) - ord('a') + 1) % 26))
                word.append(next_char)

        return word[k - 1]



ans = Solution().kthCharacter(5)
print(ans)
