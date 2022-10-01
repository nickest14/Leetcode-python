# 648. Replace Words


from typing import List


class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = {}

        def insert(word: str):
            current = trie
            for c in word:
                current = current.setdefault(c, {})
            current['$'] = word

        def replace(word: str):
            current = trie
            for c in word:
                current = current.get(c)
                if current is None:
                    break
                if '$' in current.keys():
                    return current['$']
            return word

        for root in dictionary:
            insert(root)
        return ' '.join(map(replace, sentence.split(' ')))


dictionary = ["cat", "bat", "rat"]
sentence = "the cattle was rattled by the battery"
ans = Solution().replaceWords(dictionary, sentence)
print(ans)
