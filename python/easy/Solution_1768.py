# 1768. Merge Strings Alternately


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        def gen():
            for w1, w2 in zip(word1, word2):
                yield from (w1, w2)
            yield word1[len(word2):]
            yield word2[len(word1):]

        return ''.join(gen())

# import itertools
# class Solution:
    # def mergeAlternately(self, word1: str, word2: str) -> str:
    #     return ''.join(w1 + w2 for w1, w2 in itertools.zip_longest(word1, word2, fillvalue=''))


word1 = "abcqqq"
word2 = "pqr"
ans = Solution().mergeAlternately(word1, word2)
print(ans)
