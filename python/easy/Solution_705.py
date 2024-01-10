# 705. Design HashSet


class MyHashSet:

    def __init__(self):
        self.hash_set = set()

    def add(self, key: int) -> None:
        self.hash_set.add(key)

    def remove(self, key: int) -> None:
        if self.contains(key):
            self.hash_set.remove(key)

    def contains(self, key: int) -> bool:
        return True if key in self.hash_set else False


obj = MyHashSet()
obj.add(1)
obj.add(2)
print(obj.contains(1))
obj.remove(1)
print(obj.contains(1))
