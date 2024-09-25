# 2416. Sum of Prefix Scores of Strings

from typing import List


class TrieNode:
    def __init__(self):
        self.children: dict[str, TrieNode] = {}
        self.prefix_count: int = 0


class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        root = TrieNode()

        for word in words:
            current = root
            for char in word:
                if char not in current.children:
                    current.children[char] = TrieNode()
                current = current.children[char]
                current.prefix_count += 1

        ans: list[int] = []
        for word in words:
            current = root
            count: int = 0
            for char in word:
                current = current.children[char]
                count += current.prefix_count
            ans.append(count)

        return ans


ans = Solution().sumPrefixScores(['abc', 'ab', 'bc', 'b'])
print(ans)
