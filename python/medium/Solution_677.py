# 677. Map Sum Pairs


class MapSum:
    def __init__(self):
        self.trie = {}
        self.value = {}

    def insert(self, key: str, val: int) -> None:
        delta = val - self.value.get(key, 0)
        self.value[key] = val
        node = self.trie
        for c in key:
            node = node.setdefault(c, {})
            node['val'] = node.get('val', 0) + delta

    def sum(self, prefix: str) -> int:
        node = self.trie
        for c in prefix:
            if c not in node:
                return 0
            node = node[c]
        return node['val']


# class MapSum:
#     def __init__(self):
#         self.value = {}

#     def insert(self, key: str, val: int) -> None:
#         self.value[key] = val

#     def sum(self, prefix: str) -> int:
#         return sum(self.value[key] for key in self.value if key.startswith(prefix))


# Your MapSum object will be instantiated and called as such:
obj = MapSum()
obj.insert('apple', 3)
param_1 = obj.sum('ap')
obj.insert('app', 2)
param_2 = obj.sum('ap')
print(f'{param_1=} {param_2=}')
