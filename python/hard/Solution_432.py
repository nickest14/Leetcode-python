# 432. All O`one Data Structure

class Node:
    def __init__(self, keys, count, prev=None, next=None):
        self.keys: set = keys
        self.count: int = count
        self.next: Node = next
        self.prev: Node = prev


class AllOne:
    def __init__(self):
        self.head = Node(set(), count=0)
        self.tail = Node(set(), count=float('inf'), prev=self.head)
        self.head.next = self.tail
        self.mapping: dict[str, Node] = {}

    def inc(self, key: str) -> None:
        if key in self.mapping:
            node = self.mapping[key]
            inc_cnt = node.count + 1
            if len(node.keys) == 1:
                if inc_cnt == node.next.count:
                    node.next.keys.add(key)
                    self.mapping[key] = node.next
                    node.next.prev, node.prev.next = node.prev, node.next
                else:
                    node.count = inc_cnt
            else:
                node.keys.remove(key)
                if inc_cnt == node.next.count:
                    node.next.keys.add(key)
                    self.mapping[key] = node.next
                else:
                    new_node = Node(keys={key}, count=inc_cnt, prev=node, next=node.next)
                    node.next.prev = new_node
                    node.next = new_node
                    self.mapping[key] = new_node
        else:
            if self.head.next.count == 1:
                self.head.next.keys.add(key)
                self.mapping[key] = self.head.next
            else:
                node = Node(keys={key}, count=1, prev=self.head, next=self.head.next)
                self.head.next.prev = node
                self.head.next = node
                self.mapping[key] = node

    def dec(self, key: str) -> None:
        node = self.mapping.get(key)
        if node.count == 1:
            if len(node.keys) == 1:
                node.next.prev, node.prev.next = node.prev, node.next
            else:
                node.keys.remove(key)
            del self.mapping[key]
        else:
            dec_cnt = node.count - 1
            if len(node.keys) == 1:
                if dec_cnt == node.prev.count:
                    node.prev.keys.add(key)
                    self.mapping[key] = node.prev
                    node.next.prev, node.prev.next = node.prev, node.next
                else:
                    node.count = dec_cnt
            else:
                node.keys.remove(key)
                if dec_cnt == node.prev.count:
                    node.prev.keys.add(key)
                    self.mapping[key] = node.prev
                else:
                    new_node = Node(keys={key}, count=dec_cnt, prev=node.prev, next=node)
                    node.prev.next = new_node
                    node.prev = new_node
                    self.mapping[key] = new_node

    def getMaxKey(self) -> str:
        if self.tail.prev.keys:
            return next(iter(self.tail.prev.keys))
        else:
            return ''

    def getMinKey(self) -> str:
        if self.head.next.keys:
            return next(iter(self.head.next.keys))
        else:
            return ''


obj = AllOne()
obj.inc('hello')
obj.inc('hello')
print(obj.getMaxKey())
print(obj.getMinKey())
obj.inc('leet')
print(obj.getMinKey())
obj.dec('leet')
print(obj.getMinKey())
