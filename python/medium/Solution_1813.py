# 1813. Sentence Similarity III


class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        words1: list[str] = sentence1.split()
        words2: list[str] = sentence2.split()

        if len(words1) < len(words2):
            words1, words2 = words2, words1

        start, end = 0, 0
        n1, n2 = len(words1), len(words2)

        while start < n2 and words1[start] == words2[start]:
            start += 1

        while end < n2 and words1[n1 - end - 1] == words2[n2 - end - 1]:
            end += 1

        return start + end >= n2


# ans = Solution().areSentencesSimilar('My name is Haley', 'My Haley')
ans = Solution().areSentencesSimilar('a b c d e', 'a b e')
print(ans)
