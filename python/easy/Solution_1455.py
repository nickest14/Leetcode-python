# 1455. Check If a Word Occurs As a Prefix of Any Word in a Sentence


class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        words: list[str] = sentence.split(' ')
        for i, word in enumerate(words):
            if word.startswith(searchWord):
                return i + 1
        return -1


ans = Solution().isPrefixOfWord('i love eating burger', 'burg')
print(ans)
