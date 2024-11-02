# 2490. Circular Sentence


class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        sentences: list[str] = sentence.split(' ')
        sentences.append(sentences[0])
        return all(s1[-1] == s2[0] for s1, s2 in zip(sentences, sentences[1:]))


class Solution2:
    def isCircularSentence(self, sentence: str) -> bool:
        n = len(sentence)
        if sentence[0] != sentence[n - 1]:
            return False
        for i in range(1, n - 1):
            if sentence[i] == ' ':
                if sentence[i - 1] != sentence[i + 1]:
                    return False
        return True


ans = Solution().isCircularSentence("leetcode exercises sound delightful")
print(ans)
