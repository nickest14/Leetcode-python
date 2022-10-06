# 211. Design Add and Search Words Data Structure

class WordDictionary:
    def __init__(self):
        self.trie = {}

    def addWord(self, word: str) -> None:
        node = self.trie
        for c in word:
            node = node.setdefault(c, {})
        node['$'] = True

    def search(self, word: str) -> bool:
        return self.searchNode(self.trie, word)

    def searchNode(self, node, word: str):
        for i, c in enumerate(word):
            if c == '.':
                return any(
                    self.searchNode(node[w], word[i+1:])
                    for w in node if w != '$')
            if (node := node.get(c)) is None:
                return False
        return '$' in node


# Your WordDictionary object will be instantiated and called as such:
obj = WordDictionary()
obj.addWord('app')
param_2 = obj.search('app')
print(param_2)

obj.addWord('macaxyz')
obj.addWord('macbook')
param_3 = obj.search('mac...k')
print(param_3)
