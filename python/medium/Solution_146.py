# 146. LRU Cache

class ListNode(object):
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None


class DoubleLinkedList(object):
    def __init__(self):
        self.head = ListNode(-1, 0)
        self.tail = ListNode(-1, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def remove_node(self, node: ListNode):
        if node in (self.head, self.tail):
            return None
        node.prev.next = node.next
        node.next.prev = node.prev

    def insert_head(self, node: ListNode):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node


class LRUCache:

    def __init__(self, capacity: int):
        self.lookup = {}
        self.capacity = capacity
        self.linked_list = DoubleLinkedList()

    def get(self, key: int) -> int:
        if key in self.lookup:
            node = self.lookup[key]
            self.linked_list.remove_node(node)
            self.linked_list.insert_head(node)
            return node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        node = self.lookup.get(key, ListNode(key, value))
        if key in self.lookup:
            node.val = value
            self.linked_list.remove_node(node)
        else:
            self.lookup[key] = node
        self.linked_list.insert_head(node)
        if len(self.lookup) > self.capacity:
            last = self.linked_list.tail.prev
            self.linked_list.remove_node(last)
            del self.lookup[last.key]


lru = LRUCache(2)
lru.put(1, 1)
lru.put(2, 2)
param1 = lru.get(1)  # get 1
lru.put(3, 3)  # 2 evicts cache = {1=1, 3=3}
param2 = lru.get(2)  # get -1
lru.put(4, 4)  # 1 evicts cache = {4=4, 3=3}
param3 = lru.get(1)  # get -1
print(param1, param2, param3)
