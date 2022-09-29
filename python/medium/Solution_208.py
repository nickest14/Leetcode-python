# 208. Implement Trie (Prefix Tree)


class Trie:
    def __init__(self):
        self.trie = {}

    def insert(self, word: str) -> None:
        node = self.trie
        for c in word:
            node = node.setdefault(c, {})
        node['$'] = True

    def search(self, word: str) -> bool:
        node = self.trie
        for c in word:
            if (node := node.get(c)) is None:
                return False
        return '$' in node

    def startsWith(self, prefix: str) -> bool:
        node = self.trie
        for c in prefix:
            if (node := node.get(c)) is None:
                return False
        return True


obj = Trie()
word = 'apple'
obj.insert(word)
param_2 = obj.search(word)
word2 = prefix = 'app'
param_3 = obj.search(word2)
param_4 = obj.startsWith(prefix)
obj.insert(word2)
param_5 = obj.search(word2)
print(f'{param_2=} {param_3=} {param_4=} {param_5=}')
