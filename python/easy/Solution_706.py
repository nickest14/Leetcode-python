# 706. Design HashMap


class MyHashMap:

    def __init__(self):
        self.hash_map = {}

    def put(self, key: int, value: int) -> None:
        self.hash_map[key] = value

    def get(self, key: int) -> int:
        return self.hash_map.get(key, -1)

    def remove(self, key: int) -> None:
        if key in self.hash_map:
            del self.hash_map[key]


obj = MyHashMap()
obj.put(1, 1)
obj.put(2, 2)
print(obj.get(1))
print(obj.get(3))
obj.put(2, 1)
print(obj.get(2))
obj.remove(2)
print(obj.get(2))
